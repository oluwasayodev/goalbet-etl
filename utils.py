import requests
import psycopg2
from pathlib import Path

def get_postgres_connection(host:str='localhost', port:int='5432', db_name:str='postgres', db_user:str='postgres', db_password:str='password'):
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return conn

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