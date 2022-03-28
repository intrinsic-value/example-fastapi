"""create posts table

Revision ID: 1f726ab03362
Revises: 
Create Date: 2022-03-28 10:55:43.935936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1f726ab03362"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """创建表、修改表"""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    """rollback to old version"""
    op.drop_table("posts")
    pass
