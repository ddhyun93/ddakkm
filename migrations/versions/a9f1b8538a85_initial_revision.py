"""Initial Revision

Revision ID: a9f1b8538a85
Revises: 
Create Date: 2021-09-30 12:28:52.080279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9f1b8538a85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('writer_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.ForeignKeyConstraint(['writer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_id'), 'comment', ['id'], unique=False)
    op.add_column('review', sa.Column('view_count', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    op.create_index(op.f('ix_tag_id'), 'tag', ['id'], unique=False)
    op.create_index(op.f('ix_tag_name'), 'tag', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_name'), table_name='tag')
    op.drop_index(op.f('ix_tag_id'), table_name='tag')
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_column('review', 'view_count')
    op.drop_index(op.f('ix_comment_id'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
