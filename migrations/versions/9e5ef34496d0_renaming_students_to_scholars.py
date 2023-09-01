"""Renaming students to scholars

Revision ID: 9e5ef34496d0
Revises: 
Create Date: 2023-09-01 21:24:55.440812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e5ef34496d0'
down_revision = None
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
