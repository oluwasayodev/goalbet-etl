import requests
from sqlalchemy import create_engine
from pathlib import Path
from dotenv import dotenv_values

def get_postgres_connection(host:str='localhost', port:int='5432', db_name:str='postgres', db_user:str='postgres', db_password:str='password'):
    engine = create_engine(
        f'postgresql+psycopg2://{db_user}:{db_password}@{host}:{port}/{db_name}'
    )
    return engine

def download_contents(urls: list[str]):
    """
    returns: None
    """
    extract_folder = Path("extract")
    if not extract_folder.exists():
        extract_folder.mkdir()

    for url in urls:
        filename = "".join(url.rsplit('/', maxsplit=2)[-2:])
        filepath = extract_folder/filename
        with open(f'{filepath}', 'wb') as download:
            binary_data = requests.get(url)
            download.write(binary_data.content)
        yield filepath

def extract_filename_from_path(path: str):
    return path.rstrip('/').split('.')[0]

def get_env_database_credentials():
    config = dotenv_values()
    creds = {
        'db_name': config.get('DB_NAME'),
        'db_user': config.get('DB_USER'),
        'db_password': config.get('DB_PASSWORD'),
        'host': config.get('DB_HOST'),
        'port': config.get('DB_PORT'),
    }
    return creds