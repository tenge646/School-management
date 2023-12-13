"""students table

Revision ID: 587b3be75f11
Revises: 
Create Date: 2023-12-13 15:56:46.419745

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '587b3be75f11'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'students',
        sa.Column('student_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('grades', sa.String(20)),
        sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.teacher_id'))
    )

def downgrade() -> None:
    op.drop_table('students')
