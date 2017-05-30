"""adding booklist class for M:M relationship

Revision ID: 98edc7ca0cce
Revises: 6a484410579c
Create Date: 2017-05-29 14:22:40.616605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98edc7ca0cce'
down_revision = '6a484410579c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booklists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('list_type', sa.Text(), nullable=True),
    sa.Column('comments', sa.Text(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('books_user_id_fkey', 'books', type_='foreignkey')
    op.drop_column('books', 'user_id')
    op.drop_column('books', 'list_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('list_type', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('books', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('books_user_id_fkey', 'books', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_table('booklists')
    # ### end Alembic commands ###