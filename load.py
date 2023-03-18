import psycopg2
import pandas as pd



def load_csv_to_postgres(path:str, db_connection):
    df = pd.read_csv(path)
    df.to_sql(
        name=path.rstrip('/').split('.')[0],
        if_exists='replace',
        index=False,
        con=db_connection
    )
    print(f"{path} successfully load into {path.rstrip('/').split('.')[0]} table in the database.")

