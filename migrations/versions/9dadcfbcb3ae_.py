"""empty message

Revision ID: 9dadcfbcb3ae
Revises: 
Create Date: 2019-04-24 18:28:42.358760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dadcfbcb3ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publish',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('database_name', sa.VARCHAR(length=255), nullable=True),
    sa.Column('id_types', sa.VARCHAR(length=100), nullable=False),
    sa.Column('data_file_path', sa.VARCHAR(length=255), nullable=True),
    sa.Column('data_url_path', sa.VARCHAR(), nullable=True),
    sa.Column('arc_number_min', sa.Integer(), nullable=True),
    sa.Column('arc_number_max', sa.Integer(), nullable=True),
    sa.Column('is_keywords', sa.Integer(), nullable=True),
    sa.Column('is_filter', sa.Integer(), nullable=True),
    sa.Column('is_resolve', sa.Integer(), nullable=True),
    sa.Column('is_type_top', sa.Integer(), nullable=True),
    sa.Column('is_index_page', sa.Integer(), nullable=True),
    sa.Column('is_type_page', sa.Integer(), nullable=True),
    sa.Column('is_page_all', sa.Integer(), nullable=True),
    sa.Column('is_page_curent', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('publish')
    # ### end Alembic commands ###
