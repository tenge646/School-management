"""classes table

Revision ID: 67034857b705
Revises: 
Create Date: 2023-12-14 15:05:42.696556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67034857b705'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'classes',
        sa.Column('class_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('class_name', sa.String(length=100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('classes')
