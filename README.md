# Description
This repo contains code for an ETL pipeline which extracts data from [goalbet](https://www.football-data.co.uk/englandm). The website contains links to csv files containing data about football matches in England at various seasons. The links to the csv files were scraped using the python `requests`, `re` and `beautifulsoup` libraries.

# Run Pipeline
To run the pipeline, create a virtual environment and install the requirements file using the command below
```bash
pip install -r requirements.txt
```

The run the pipeline using the command:
```python
python main.py
```