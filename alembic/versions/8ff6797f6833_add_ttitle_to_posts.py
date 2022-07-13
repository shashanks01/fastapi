"""Add ttitle to posts

Revision ID: 8ff6797f6833
Revises: 44b786af5f0d
Create Date: 2022-07-12 22:02:37.761406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ff6797f6833'
down_revision = '44b786af5f0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'title')
    pass