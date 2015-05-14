"""table "emails"

Revision ID: 2580663da150
Revises: 4b95d8299c89
Create Date: 2015-05-13 22:58:42.455202

"""

# revision identifiers, used by Alembic.
revision = '2580663da150'
down_revision = '4b95d8299c89'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('address', 'owner_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    ### end Alembic commands ###
