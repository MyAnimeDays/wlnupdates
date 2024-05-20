"""Make tlgroup altname group column not nullable

Revision ID: 45dabd9fe38d
Revises: 276133b04e90
Create Date: 2020-10-15 06:11:35.139484

"""

# revision identifiers, used by Alembic.
revision = '45dabd9fe38d'
down_revision = '276133b04e90'

from alembic import op
from sqlalchemy.sql import table
from sqlalchemy.sql import column
import sqlalchemy as sa
import citext
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.dialects.postgresql import JSONB


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    role = table('alternatetranslatornames', column('group'))
    op.alter_column('alternatetranslatornames', 'group', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass