"""create user table

Revision ID: dd7a81e8dcd9
Revises: 
Create Date: 2021-08-10 19:45:29.306210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7a81e8dcd9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(80), nullable=True),
        sa.Column('last_name', sa.String(80), nullable=True),
        sa.Column('username', sa.String(150), nullable=False),
        
    )


def downgrade():
    pass
