"""change column names

Revision ID: 4366a593d4ce
Revises: 7496bd942824
Create Date: 2023-04-19 07:40:03.026503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4366a593d4ce'
down_revision = '7496bd942824'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('state', sa.String(), nullable=True))

    with op.batch_alter_table('rounds', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tournament_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_rounds_tournament_id_tournaments'), 'tournaments', ['tournament_id'], ['id'])
        batch_op.drop_column('par')
        batch_op.drop_column('score')

    with op.batch_alter_table('scorecards', schema=None) as batch_op:
        batch_op.drop_constraint('fk_scorecards_tournament_id_tournaments', type_='foreignkey')
        batch_op.drop_column('tournament_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scorecards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tournament_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_scorecards_tournament_id_tournaments', 'tournaments', ['tournament_id'], ['id'])

    with op.batch_alter_table('rounds', schema=None) as batch_op:
        batch_op.add_column(sa.Column('score', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('par', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_rounds_tournament_id_tournaments'), type_='foreignkey')
        batch_op.drop_column('tournament_id')

    with op.batch_alter_table('courses', schema=None) as batch_op:
        batch_op.drop_column('state')
        batch_op.drop_column('city')

    # ### end Alembic commands ###
