"""empty message

Revision ID: 1a68ae595b94
Revises: None
Create Date: 2016-10-28 13:43:24.789707

"""

# revision identifiers, used by Alembic.
revision = '1a68ae595b94'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    ### end Alembic commands ###
