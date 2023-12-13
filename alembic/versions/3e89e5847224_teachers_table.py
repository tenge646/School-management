"""teachers table

Revision ID: 3e89e5847224
Revises: 587b3be75f11
Create Date: 2023-12-13 16:15:46.195360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e89e5847224'
down_revision: Union[str, None] = '587b3be75f11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'teachers',
        sa.Column('teacher_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('class', sa.String(20)),
    )

def downgrade() -> None:
    op.drop_table('teachers')
