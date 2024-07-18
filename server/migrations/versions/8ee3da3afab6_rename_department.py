"""rename department

Revision ID: 8ee3da3afab6
Revises: 961aad6545d4
Create Date: 2024-07-18 13:31:26.796706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee3da3afab6'
down_revision = '961aad6545d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department','departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments','department')
    # ### end Alembic commands ###
