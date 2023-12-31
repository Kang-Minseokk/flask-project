"""empty message

Revision ID: da439189113a
Revises: c3eb3a430cfb
Create Date: 2023-07-31 17:34:22.873659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da439189113a'
down_revision = 'c3eb3a430cfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('modify_date', sa.DATETIME(), nullable=True),
    sa.Column('question_id', sa.INTEGER(), nullable=True),
    sa.Column('answer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name='fk_comment_answer_id_answer', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='fk_comment_question_id_question', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_comment_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pk_comment')
    )
    # ### end Alembic commands ###
