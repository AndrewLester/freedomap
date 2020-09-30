"""Add timestamp column

Revision ID: f817f2da0d56
Revises: 
Create Date: 2020-10-13 18:17:20.837304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f817f2da0d56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('protest',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('lat', sa.Float(precision=7), nullable=True),
    sa.Column('lng', sa.Float(precision=7), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('protestsubmission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('protest_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('lat', sa.Float(precision=7), nullable=True),
    sa.Column('lng', sa.Float(precision=7), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=True),
    sa.Column('size', sa.String(length=120), nullable=True),
    sa.Column('issue_locality', sa.String(length=120), nullable=True),
    sa.Column('issue_type', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['protest_id'], ['protest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('protestsubmission')
    op.drop_table('protest')
    # ### end Alembic commands ###