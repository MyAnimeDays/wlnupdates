"""empty message

Revision ID: d10a5fc828b8
Revises: ff3d74ef531e
Create Date: 2017-08-02 22:23:33.179981

"""

# revision identifiers, used by Alembic.
revision = 'd10a5fc828b8'
down_revision = 'ff3d74ef531e'

from alembic import op
import sqlalchemy as sa
import citext


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_serieschanges_srccol', table_name='serieschanges')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_serieschanges_srccol', 'serieschanges', ['srccol'], unique=False)
    ### end Alembic commands ###
