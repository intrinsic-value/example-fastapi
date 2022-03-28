"""sqlalchemy对应的类定义
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    """返回类型使用"""

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # 从数据库取出数据，需要转回字典类型，
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    """加密使用的私钥

    Args:
        BaseModel (_type_): _description_
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """加密附加的数据

    Args:
        BaseModel (_type_): _description_
    """

    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
