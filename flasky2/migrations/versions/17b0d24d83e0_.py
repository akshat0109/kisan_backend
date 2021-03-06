"""empty message

Revision ID: 17b0d24d83e0
Revises: None
Create Date: 2018-04-25 02:28:36.675000

"""

# revision identifiers, used by Alembic.
revision = '17b0d24d83e0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('estd', sa.Date(), nullable=False),
    sa.Column('location', sa.String(length=128), nullable=False),
    sa.Column('emi', sa.Integer(), nullable=False),
    sa.Column('rate_int', sa.Integer(), nullable=False),
    sa.Column('Contact_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person_address',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('home_address', sa.String(length=128), nullable=False),
    sa.Column('district', sa.String(length=128), nullable=False),
    sa.Column('state', sa.String(length=128), nullable=False),
    sa.Column('pincode', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('dob', sa.String(length=128), nullable=False),
    sa.Column('gender', sa.Enum('M', 'F'), nullable=True),
    sa.Column('phone_no', sa.String(length=16), nullable=False),
    sa.Column('email_id', sa.String(length=128), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['person_address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('policy',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.Column('maturity_period', sa.Integer(), nullable=True),
    sa.Column('documents_reqd', sa.String(length=128), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=False),
    sa.Column('amtdeposited', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('field',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('area', sa.Integer(), nullable=False),
    sa.Column('price_sqft', sa.Integer(), nullable=False),
    sa.Column('annual_incg', sa.Integer(), nullable=False),
    sa.Column('crops_g', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('machinery',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_by', sa.String(length=64), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('spec', sa.String(length=128), nullable=True),
    sa.Column('Date_mfg', sa.Date(), nullable=False),
    sa.Column('warranty', sa.String(length=128), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('machinery')
    op.drop_table('images')
    op.drop_table('field')
    op.drop_table('policy')
    op.drop_table('person')
    op.drop_table('person_address')
    op.drop_table('company')
    ### end Alembic commands ###
