from extract import extract
from transform import extract_columns

if __name__ == '__main__':
    downloaded_paths = extract()
    for path in downloaded_paths:
        columns_to_extract = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
        try:
                transformed_path = extract_columns(path, columns_to_extract)
        except KeyError:
            columns_to_extract = set(columns_to_extract).difference({'Time'})
            columns_to_extract = list(columns_to_extract)
            transformed_path = extract_columns(path, columns_to_extract)
        finally:
             print("Done: ", transformed_path)
