"""subjects table

Revision ID: 00b32b955637
Revises: 3e89e5847224
Create Date: 2023-12-13 16:40:25.530820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00b32b955637'
down_revision: Union[str, None] = '3e89e5847224'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'subjects',
        sa.Column('subject_id', sa.Integer, primary_key=True),
        sa.Column('subject_name', sa.String(50)),
    )

def downgrade() -> None:
    op.drop_table('subjects')

