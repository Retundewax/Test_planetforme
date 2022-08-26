import requests
import pytest
URL = 'https://reqres.in/api/users'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
DANNIE = {
    'name': 'oleg',
    'job': 'president'
}


def post_zapros():
    pp = requests.post(URL, data=DANNIE).json()
    return pp

otvet = post_zapros()

def test_name_and_job():
    assert otvet['name'] == DANNIE['name']
    assert otvet['job'] == DANNIE['job']
    print(otvet['name'], otvet['job'])
    print (otvet)
