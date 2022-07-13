"""add the last few colums to posts

Revision ID: dfc989d01fed
Revises: de372fb9cbff
Create Date: 2022-07-12 22:14:39.634486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc989d01fed'
down_revision = 'de372fb9cbff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',  sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
