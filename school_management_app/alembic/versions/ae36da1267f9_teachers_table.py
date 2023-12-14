"""teachers table

Revision ID: ae36da1267f9
Revises: 490aa5f84c1f
Create Date: 2023-12-13 22:17:15.186915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae36da1267f9'
down_revision: Union[str, None] = '490aa5f84c1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'teachers',
        sa.Column('teacher_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('class', sa.String(length=255), nullable=True),
    )

def downgrade() -> None:
    op.drop_table('teachers')
