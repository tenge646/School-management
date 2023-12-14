"""students table

Revision ID: 490aa5f84c1f
Revises: faa68600fb03
Create Date: 2023-12-13 22:16:24.142463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '490aa5f84c1f'
down_revision: Union[str, None] = 'faa68600fb03'
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
