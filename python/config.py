"""Shared paths and database configuration for the project scripts."""

import os
from pathlib import Path
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
IMAGE_DIR = PROJECT_ROOT / "image"
REPORT_DIR = PROJECT_ROOT / "report"

load_dotenv(PROJECT_ROOT / ".env")


def create_mysql_engine():
    """Create a SQLAlchemy engine without storing credentials in source code."""

    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    database = os.getenv("MYSQL_DATABASE", "superstore_analysis")

    if not password:
        raise RuntimeError(
            "MYSQL_PASSWORD is not configured. Copy .env.example to .env "
            "and enter your local MySQL password."
        )

    connection_url = (
        f"mysql+pymysql://{quote_plus(user)}:{quote_plus(password)}"
        f"@{host}:{port}/{database}?charset=utf8mb4"
    )
    return create_engine(connection_url)

