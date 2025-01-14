"""Add name column to cats and owners tables

Revision ID: a2e0627d3287
Revises: a9a92612487f
Create Date: 2024-12-30 09:28:58.967126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2e0627d3287'
down_revision = 'a9a92612487f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    with op.batch_alter_table('owners', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('owners', schema=None) as batch_op:
        batch_op.drop_column('name')

    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
