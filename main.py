from extract import extract
from transform import extract_columns, add_time_column, format_date_column
from load import load_csv_to_postgres
from utils import get_postgres_connection

if __name__ == '__main__':
    downloaded_paths = extract()
    columns_to_extract = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
    for path in downloaded_paths:
        try:
            transformed_path = extract_columns(path, columns_to_extract)
        except KeyError:
            columns_to_extract = set(columns_to_extract).difference({'Time'})
            columns_to_extract = list(columns_to_extract)
            transformed_path = extract_columns(path, columns_to_extract)
            transformed_path = add_time_column(transformed_path)
            transformed_path = format_date_column(transformed_path, 'Date')

        finally:
            conn = get_postgres_connection(db_name='footballdb')
            load_csv_to_postgres(transformed_path, conn)
