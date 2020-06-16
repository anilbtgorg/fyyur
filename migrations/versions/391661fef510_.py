"""empty message

Revision ID: 391661fef510
Revises: 80f5dbac65d3
Create Date: 2020-06-12 23:07:10.159902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391661fef510'
down_revision = '80f5dbac65d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
