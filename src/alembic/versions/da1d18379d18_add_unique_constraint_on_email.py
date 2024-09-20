"""Add unique constraint on Email

Revision ID: da1d18379d18
Revises: f8d5469d79f3
Create Date: 2024-09-20 21:04:42.408060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da1d18379d18'
down_revision: Union[str, None] = 'f8d5469d79f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_user_email'), 'user', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_user_email'), 'user', type_='unique')
    # ### end Alembic commands ###
