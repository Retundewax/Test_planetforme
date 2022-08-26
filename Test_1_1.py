import requests
import re

URL = 'https://reqres.in/api/users?page=2'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_request():
    req = requests.get(URL, headers=HEADERS)
    return req

perechen_akkauntov = get_request().json()['data']

def test_all_data_got():
    assert len(perechen_akkauntov) == 6
    for i in perechen_akkauntov:
        assert (len(i)) == 5
    print(perechen_akkauntov)

def test_validatsiya_email():
    for i in perechen_akkauntov:
        j = i['email']
        b = re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', j)
        assert b.group(0) == j
        print(f'{j} почта валидна')

