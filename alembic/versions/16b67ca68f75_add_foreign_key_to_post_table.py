"""add foreign_key to post table

Revision ID: 16b67ca68f75
Revises: 9203d38d4db0
Create Date: 2022-03-28 11:20:26.577560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "16b67ca68f75"
down_revision = "9203d38d4db0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
