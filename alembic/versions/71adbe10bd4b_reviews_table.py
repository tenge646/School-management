"""reviews table

Revision ID: 71adbe10bd4b
Revises: 
Create Date: 2023-12-13 10:52:16.885261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71adbe10bd4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'reviews',
        sa.Column('customer_name', sa.String()),
        sa.Column('rating', sa.Integer()),
        sa.Column('comment', sa.String()),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'))  # Assuming a foreign key to users table
    )

def downgrade() -> None:
    op.drop_table('reviews')
