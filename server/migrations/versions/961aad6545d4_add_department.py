"""add Department

Revision ID: 961aad6545d4
Revises: 4832e14eb9de
Create Date: 2024-07-18 13:13:09.481817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '961aad6545d4'
down_revision = '4832e14eb9de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
