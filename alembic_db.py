"""create users table

Revision ID: 20d84661476e
Revises:
Create Date: 2018-01-30 11:34:58.358723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d84661476e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'users',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('login', sa.String(50), nullable=False),
    sa.Column('password', sa.String(50), nullable=False),
    sa.Column('email', sa.String(50), nullable=False),
    sa.Column('phone', sa.Integer)
    )


def downgrade():
    op.drop_table('users')
