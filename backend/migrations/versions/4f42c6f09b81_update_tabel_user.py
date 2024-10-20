"""update tabel user

Revision ID: 4f42c6f09b81
Revises: 158166271eb1
Create Date: 2024-10-06 18:57:15.012395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f42c6f09b81'
down_revision = '158166271eb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('level', sa.BigInteger(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('level')

    # ### end Alembic commands ###
