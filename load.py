import pandas as pd



def load_csv_to_postgres(path:str, db_connection):
    df = pd.read_csv(path)
    df.columns = [x.lower() for x in df.columns]
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format="%d/%m/%Y %H:%M")
    df.drop(columns=['date', 'time'], inplace=True)
    df.to_sql(
        name='goalbet',
        if_exists='append',
        index=False,
        con=db_connection
    )
    print(f"{path} successfully load into {path.rstrip('/').split('.')[0]} table in the database.")

