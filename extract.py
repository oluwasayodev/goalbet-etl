import re
import requests
from bs4 import BeautifulSoup
from utils import download_contents
import pathlib

def extract(pattern: str = r'(mmz4281/(1920/E[02]|0203/E1)\.csv)'):

    url = 'https://www.football-data.co.uk'

    country = 'englandm'

    response = requests.get(url=f'{url}/{country}')

    soup = BeautifulSoup(markup=response.content, features='lxml')

    string_regex = re.compile(pattern)

    anchor_tags = soup.find_all(name='a', attrs={'href': string_regex})

    media_urls = list(map(lambda x: f'{url}/{string_regex.search(str(x)).group(0)}', anchor_tags))

    paths = download_contents(media_urls)

    for path in paths:
        yield path

    