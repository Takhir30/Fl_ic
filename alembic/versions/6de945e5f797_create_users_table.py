"""create users table

Revision ID: 6de945e5f797
Revises:
Create Date: 2018-02-01 11:36:03.672604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6de945e5f797'
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
    sa.Column('phone', sa.String(20))
    )


def downgrade():
    op.drop_table('users')
