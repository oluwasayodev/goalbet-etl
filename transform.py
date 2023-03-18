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