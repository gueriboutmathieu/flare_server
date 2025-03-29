"""add statements

Revision ID: f160bf5fa952
Revises:
Create Date: 2025-01-26 14:22:35.598335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import VECTOR  # pyright: ignore


# revision identifiers, used by Alembic.
revision: str = "f160bf5fa952"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Activate vector extension
    op.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    # Create statements table
    op.create_table(
        "statements",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("vector", VECTOR(dim=1536), nullable=False),  # pyright: ignore
        sa.PrimaryKeyConstraint("id")
    )

    # Create vector index
    op.execute("CREATE INDEX IF NOT EXISTS vector_idx ON statements USING ivfflat (vector) WITH (lists = 50);")


def downgrade() -> None:
    # Delete vector index
    op.execute("DROP INDEX IF EXISTS vector_idx;")

    # Delete statements table
    op.drop_table("statements")

    # Deactivate vector extension
    op.execute("DROP EXTENSION IF EXISTS vector;")
