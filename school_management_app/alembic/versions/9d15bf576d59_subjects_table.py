"""subjects table

Revision ID: 9d15bf576d59
Revises: ae36da1267f9
Create Date: 2023-12-13 22:18:09.137502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d15bf576d59'
down_revision: Union[str, None] = 'ae36da1267f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'subjects',
        sa.Column('subject_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('subject_name', sa.String(length=255), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('subjects')