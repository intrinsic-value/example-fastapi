"""add user table

Revision ID: 9203d38d4db0
Revises: bd8cc7f4eef3
Create Date: 2022-03-28 11:12:28.640328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9203d38d4db0"
down_revision = "bd8cc7f4eef3"
branch_labels = None
depends_on = None


def upgrade():
    """创建表、修改表"""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    """rollback to old version"""
    op.drop_table("users")
    pass
