"""initial

Revision ID: d53f89a90559
Revises: 
Create Date: 2023-11-01 10:17:14.016924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd53f89a90559'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mnemonic', sa.String(length=200), nullable=True),
    sa.Column('xpub', sa.String(length=200), nullable=True),
    sa.Column('btc_address', sa.String(length=50), nullable=True),
    sa.Column('eth_address', sa.String(length=50), nullable=True),
    sa.Column('trade', sa.String(length=50), nullable=True),
    sa.Column('token', sa.String(length=100), nullable=True),
    sa.Column('store', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.String(length=16), nullable=False),
    sa.Column('seller', sa.String(length=20), nullable=True),
    sa.Column('buyer', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('invoice', sa.String(length=50), nullable=True),
    sa.Column('currency', sa.String(length=32), nullable=True),
    sa.Column('coin', sa.String(length=32), nullable=True),
    sa.Column('wallet', sa.String(length=50), nullable=True),
    sa.Column('payment_status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.String(length=32), nullable=True),
    sa.Column('updated_at', sa.String(length=32), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('agent_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat', sa.String(length=20), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('affiliates',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disputes',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('complaint', sa.String(length=162), nullable=True),
    sa.Column('created_on', sa.String(length=32), nullable=True),
    sa.Column('trade_id', sa.String(length=16), nullable=True),
    sa.ForeignKeyConstraint(['trade_id'], ['trades.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('disputes')
    op.drop_table('affiliates')
    op.drop_table('users')
    op.drop_table('trades')
    op.drop_table('agent')
    # ### end Alembic commands ###
