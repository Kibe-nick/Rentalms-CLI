"""Initial migration

Revision ID: b9051e36169c
Revises: 
Create Date: 2024-09-23 15:18:47.796076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9051e36169c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Create a new table with the desired schema
    op.create_table(
        'new_apartments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),  # This will match your desired schema
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('num_rooms', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO new_apartments (id, name, location, num_rooms) SELECT id, name, NULL, NULL FROM apartments')

    # Drop the old table
    op.drop_table('apartments')

    # Rename the new table to the old table's name
    op.rename_table('new_apartments', 'apartments')

    # Create indexes if needed
    op.create_index(op.f('ix_apartments_id'), 'apartments', ['id'], unique=False)
    op.create_index(op.f('ix_apartments_name'), 'apartments', ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    # Create a new table for downgrade
    op.create_table(
        'new_apartments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),  # Change to NOT NULL for downgrade
        sa.Column('address', sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data back if needed (might be tricky if `address` is not in the original table)
    op.execute('INSERT INTO new_apartments (id, name, address) SELECT id, name, NULL FROM apartments')

    # Drop the current table
    op.drop_table('apartments')

    # Rename the new table back
    op.rename_table('new_apartments', 'apartments')

    # Drop indexes if they were created
    op.drop_index(op.f('ix_apartments_name'), table_name='apartments')
    op.drop_index(op.f('ix_apartments_id'), table_name='apartments')

    # ### end Alembic commands ###

    
