"""staffs table

Revision ID: b187219d6942
Revises: 71adbe10bd4b
Create Date: 2023-12-13 10:54:31.299093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b187219d6942'
down_revision = '71adbe10bd4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'staffs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('day', sa.String()),
        sa.Column('chef', sa.String()),
        sa.Column('waiter', sa.String())
    )

def downgrade() -> None:
    op.drop_table('staffs')

