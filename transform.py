import pandas as pd
from pathlib import Path

def extract_columns(path: str, columns: list[str]):
    print("The path: ", path)
    fp = Path(path)
    df = pd.read_csv(path, on_bad_lines='warn')
    df = df.loc[:, columns]
    cp = Path('transformed')
    if not cp.exists():
        cp.mkdir()
    df.to_csv(f'{cp.name}/{fp.name}', index=False)
    return f'{cp.name}/{fp.name}'

def format_date_column(path: str, date_column_name='date', format='%d/%m/%Y'):
    fp = Path(path)
    df = pd.read_csv(path, parse_dates=[date_column_name], on_bad_lines='warn')
    df[date_column_name] = df[date_column_name].dt.strftime('%d/%m/%Y')
    cp = Path('transformed')
    if not cp.exists():
        cp.mkdir()
    df.to_csv(f'{cp.name}/{fp.name}', index=False)
    return f'{cp.name}/{fp.name}'

def add_time_column(path):
    fp = Path(path)
    df = pd.read_csv(path, on_bad_lines='warn')
    df["Time"] = "00:00"
    cp = Path('transformed')
    if not cp.exists():
        cp.mkdir()
    df.to_csv(f'{cp.name}/{fp.name}', index=False)
    return f'{cp.name}/{fp.name}'