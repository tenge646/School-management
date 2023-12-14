"""subjects table

Revision ID: 309bed5b61f1
Revises: 5e7280828254
Create Date: 2023-12-14 15:10:46.097127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '309bed5b61f1'
down_revision: Union[str, None] = '5e7280828254'
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
