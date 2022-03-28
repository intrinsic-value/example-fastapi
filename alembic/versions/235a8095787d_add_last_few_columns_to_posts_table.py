"""add last few columns to posts table

Revision ID: 235a8095787d
Revises: 16b67ca68f75
Create Date: 2022-03-28 13:03:20.719049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "235a8095787d"
down_revision = "16b67ca68f75"
branch_labels = None
depends_on = None


def upgrade():
    """创建表、修改表"""
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )
    pass


def downgrade():
    """rollback to old version"""
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
