"""meals table

Revision ID: d37f7fae847c
Revises: b187219d6942
Create Date: 2023-12-13 10:56:08.901177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd37f7fae847c'
down_revision = 'b187219d6942'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'meals',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('day', sa.String()),
        sa.Column('meals', sa.String()),
        sa.Column('drinks', sa.String())
    )

def downgrade() -> None:
    op.drop_table('meals')