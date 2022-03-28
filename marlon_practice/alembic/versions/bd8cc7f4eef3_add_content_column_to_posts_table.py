"""add content column to posts table

Revision ID: bd8cc7f4eef3
Revises: 1f726ab03362
Create Date: 2022-03-28 11:05:14.182938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bd8cc7f4eef3"
down_revision = "1f726ab03362"
branch_labels = None
depends_on = None


def upgrade():
    """创建表、修改表"""
    op.add_column(
        "posts",
        sa.Column("content", sa.Integer(), nullable=False, primary_key=True),
    )
    pass


def downgrade():
    """rollback to old version"""
    op.drop_column("posts", "content")
    pass
