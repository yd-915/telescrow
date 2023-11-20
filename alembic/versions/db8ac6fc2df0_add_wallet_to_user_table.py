"""add wallet to user table

Revision ID: db8ac6fc2df0
Revises: 620f0095b52d
Create Date: 2023-11-12 02:42:07.519609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db8ac6fc2df0'
down_revision: Union[str, None] = '620f0095b52d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('wallet', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'wallet')
    # ### end Alembic commands ###