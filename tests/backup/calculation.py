import pytest
from app.calculations import (
    subtract,
    add,
    multiply,
    divide,
    BankAccount,
    InsufficientFunds,
)

# 设定常用对象，用这个函数代表一个常用对象
@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


# 必须用 test_ 命名，才能自动发现
# 使用pytest的参数化装饰，多次测试
@pytest.mark.parametrize("num1, num2, expected", [(3, 2, 5), (7, 1, 8), (12, 4, 16)])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_substract():
    assert subtract(7, 3) == 4


def test_multiply():
    assert multiply(7, 3) == 21


def test_divide():
    assert divide(20, 4) == 5


# 测试初始化0元账户
def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0


# 测试初始化50元账户
def test_bank_set_initial_amount(bank_account):

    assert bank_account.balance == 50


def test_withdraw(bank_account):

    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):

    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):

    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize(
    "deposited, withdrew, expected",
    [
        (200, 100, 100),
        (50, 10, 40),
        (1200, 200, 1000),
        # (10, 50, -40),
    ],
)
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    # 如果pytest出现这种 InsufficientFunds 错误，就测试通过；其他错误就失败；同时测试错误的类型
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
