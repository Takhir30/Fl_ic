"""create users table

Revision ID: 7b9f68bb692a
Revises:
Create Date: 2018-02-01 14:20:17.551405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9f68bb692a'
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
