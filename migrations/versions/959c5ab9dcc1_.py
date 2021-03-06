"""empty message

Revision ID: 959c5ab9dcc1
Revises: 
Create Date: 2019-05-15 13:31:05.082950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959c5ab9dcc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bbs_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login_name', sa.String(length=16), nullable=False, comment='登录的用户名'),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('nickname', sa.String(length=16), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('last_login_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login_name')
    )
    op.create_table('bbs_problem',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True, comment='是否置顶'),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('change_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['bbs_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bbs_solve',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('answer', sa.TEXT(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('problem', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['problem'], ['bbs_problem.id'], ),
    sa.ForeignKeyConstraint(['user'], ['bbs_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bbs_solve')
    op.drop_table('bbs_problem')
    op.drop_table('bbs_users')
    # ### end Alembic commands ###
