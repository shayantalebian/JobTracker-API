from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# 1. Import your settings and SQLAlchemy Base
from app.core.config import settings
from app.core.database import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# 2. Dynamically set the database URL from your settings
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 3. Connect Alembic to your SQLAlchemy metadata for 'autogenerate' support
target_metadata = Base.metadata

# ... (keep the rest of the default run_migrations_offline and run_migrations_online functions exactly as they are)
