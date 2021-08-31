import os


def get(key: str) -> str:
    return os.environ[key]


def get_database_connection_uri() -> str:
    return (
        "postgresql+psycopg2://"
        f"{get('POSTGRES_USER')}:"
        f"{get('POSTGRES_PASSWORD')}@"
        f"{get('POSTGRES_HOST')}:"
        f"{get('POSTGRES_PORT')}/"
        f"{get('POSTGRES_DB')}"
    )


def get_root_dir() -> str:
    current_path = os.path.abspath(__file__)
    return os.path.dirname(current_path)
