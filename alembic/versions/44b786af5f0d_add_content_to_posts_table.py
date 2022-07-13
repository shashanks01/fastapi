"""Add content to posts table

Revision ID: 44b786af5f0d
Revises: fc7cc497f7c3
Create Date: 2022-07-12 21:57:38.965923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44b786af5f0d'
down_revision = 'fc7cc497f7c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
