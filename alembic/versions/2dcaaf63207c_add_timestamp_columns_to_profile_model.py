"""Add timestamp columns to Profile model

Revision ID: 2dcaaf63207c
Revises: 90f3e16b5d24
Create Date: 2024-10-17 09:09:31.166346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dcaaf63207c'
down_revision: Union[str, None] = '90f3e16b5d24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('profiles', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'updated_at')
    op.drop_column('profiles', 'created_at')
    # ### end Alembic commands ###
