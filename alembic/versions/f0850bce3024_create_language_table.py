"""create language table

Revision ID: f0850bce3024
Revises: ec2cef051060
Create Date: 2020-10-20 18:29:18.649874

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0850bce3024'
down_revision = 'ec2cef051060'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "language",
        sa.Column("id", sa.Integer(), nullable=False),

        sa.Column("code", sa.VARCHAR(3), nullable=False, unique=True),
        sa.Column("name", sa.VARCHAR(64), nullable=True),
        sa.Column("native_name", sa.VARCHAR(64), nullable=True),

        sa.Column("created_at", sa.TIMESTAMP, nullable=False, default=datetime.now().timestamp()),
        sa.Column("deleted_at", sa.TIMESTAMP(), nullable=True),

        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(op.f("index_language_code"), "language", ["code"])
    op.create_index(op.f("index_language_name"), "language", ["name"])
    op.create_index(op.f("index_language_native_name"), "language", ["native_name"])
    op.create_index(op.f("index_language_created_at"), "language", ["created_at"])
    op.create_index(op.f("index_language_deleted_at"), "language", ["deleted_at"])


def downgrade():
    op.drop_index("index_language_code", table_name="language")
    op.drop_index("index_language_name", table_name="language")
    op.drop_index("index_language_native_name", table_name="language")
    op.drop_index("index_language_created_at", table_name="language")
    op.drop_index("index_language_deleted_at", table_name="language")
    op.drop_table("language")
