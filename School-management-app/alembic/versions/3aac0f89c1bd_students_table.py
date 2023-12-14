"""students table

Revision ID: 3aac0f89c1bd
Revises: 67034857b705
Create Date: 2023-12-14 15:07:13.108565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3aac0f89c1bd'
down_revision: Union[str, None] = '67034857b705'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('student_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('grades', sa.Integer(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['teacher_id'], ['teachers.teacher_id'])
    )

def downgrade() -> None:
    op.drop_table('students')

