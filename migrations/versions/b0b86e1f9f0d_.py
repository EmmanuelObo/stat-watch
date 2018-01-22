"""empty message

Revision ID: b0b86e1f9f0d
Revises: eb083f9e5bfc
Create Date: 2018-01-21 22:11:22.993040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0b86e1f9f0d'
down_revision = 'eb083f9e5bfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('playerprofile', sa.Column('prior', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('playerprofile', 'prior')
    # ### end Alembic commands ###
