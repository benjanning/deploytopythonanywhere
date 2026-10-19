"""Database connection settings loaded from environment variables.

Configure DB_HOST, DB_USER, DB_PASSWORD and DB_NAME in the deployment
environment. Never commit real passwords to GitHub.
"""
import os

mysql = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", ""),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", ""),
}
