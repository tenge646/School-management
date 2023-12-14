"""classes table

Revision ID: faa68600fb03
Revises:
Create Date: 2023-12-13 22:14:22.490893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'faa68600fb03'
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
