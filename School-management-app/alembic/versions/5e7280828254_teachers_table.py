"""teachers table

Revision ID: 5e7280828254
Revises: 3aac0f89c1bd
Create Date: 2023-12-14 15:09:18.055274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e7280828254'
down_revision: Union[str, None] = '3aac0f89c1bd'
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