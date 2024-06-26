"""empty message

Revision ID: 26f794d5f460
Revises: 4705e256f9b4
Create Date: 2024-04-29 00:30:05.902241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26f794d5f460'
down_revision: Union[str, None] = '4705e256f9b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('educator_data', sa.Column('last_name', sa.String(), nullable=False))
    op.drop_column('educator_data', 'second_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('educator_data', sa.Column('second_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('educator_data', 'last_name')
    # ### end Alembic commands ###
