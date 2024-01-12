"""empty message

Revision ID: 391031fe59d9
Revises: 11e8ed6122fb
Create Date: 2024-01-12 16:19:21.541018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391031fe59d9'
down_revision = '11e8ed6122fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libraries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('contact_info', sa.String(), nullable=True),
    sa.Column('reader_library_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reader_library_id'], ['libraries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('staff_library_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['staff_library_id'], ['libraries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('edition', sa.String(), nullable=True),
    sa.Column('condition', sa.String(), nullable=True),
    sa.Column('library_id', sa.Integer(), nullable=True),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['library_id'], ['libraries.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('my_library_id', sa.Integer(), nullable=True),
    sa.Column('my_reader_id', sa.Integer(), nullable=True),
    sa.Column('my_book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['my_book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['my_library_id'], ['libraries.id'], ),
    sa.ForeignKeyConstraint(['my_reader_id'], ['readers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('books')
    op.drop_table('staff')
    op.drop_table('readers')
    op.drop_table('libraries')
    # ### end Alembic commands ###
