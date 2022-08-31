"""add new models

Revision ID: 40fb9e1858df
Revises: dab564422998
Create Date: 2022-08-31 17:11:34.114013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40fb9e1858df'
down_revision = 'dab564422998'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('modules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('courses_modules',
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['module_id'], ['modules.id'], )
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=5), nullable=True),
    sa.Column('lector_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['lector_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.Column('module_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['module_id'], ['modules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups_students',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups_students')
    op.drop_table('lessons')
    op.drop_table('groups')
    op.drop_table('courses_modules')
    op.drop_table('modules')
    op.drop_table('courses')
    # ### end Alembic commands ###