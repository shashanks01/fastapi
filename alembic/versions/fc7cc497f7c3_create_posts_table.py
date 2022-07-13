"""create posts table

Revision ID: fc7cc497f7c3
Revises: 
Create Date: 2022-07-12 16:03:07.868951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc7cc497f7c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id', sa.Integer, nullable=False,primary_key=True))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
