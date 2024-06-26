"""empty message

Revision ID: 019d38caaada
Revises: 00be9346fec4
Create Date: 2023-12-24 22:26:01.332241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019d38caaada'
down_revision = '00be9346fec4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problem_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('score', sa.Double(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('problem_history', schema=None) as batch_op:
        batch_op.drop_column('score')

    # ### end Alembic commands ###
