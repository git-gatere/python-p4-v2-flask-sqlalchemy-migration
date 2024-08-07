"""rename location

Revision ID: 70924cff16ee
Revises: 8ee3da3afab6
Create Date: 2024-07-18 13:53:56.823561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70924cff16ee'
down_revision = '8ee3da3afab6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments','address',new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')
    # ### end Alembic commands ###
