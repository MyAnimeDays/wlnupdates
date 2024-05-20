"""empty message

Revision ID: 10dd5ff41d2b
Revises: e276fd17b9b4
Create Date: 2016-08-12 22:34:02.402949

"""

# revision identifiers, used by Alembic.
revision = '10dd5ff41d2b'
down_revision = 'e276fd17b9b4'

from alembic import op
import sqlalchemy as sa
import citext
from sqlalchemy.dialects import postgresql

def upgrade():
    series_sort_enum = postgresql.ENUM('parsed_title_order', 'chronological_order', name='series_sort_mode_enum')
    series_sort_enum.create(op.get_bind(), checkfirst=False)



def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
