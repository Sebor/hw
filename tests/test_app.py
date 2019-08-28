import requests
import os
import datetime

url = os.getenv('APP_URL', 'http://localhost:8080/hello')

put_common_data = ['sergey', '2009-09-13']
put_today_data = ['fedor', '-'.join(['1999', str(datetime.date.today().month), str(datetime.date.today().day)])]
put_wrong_data = ['valentin', '29/2/2038']

get_today_data = 'fedor'
get_common_data = 'sergey'
get_wrong_data = 'oleg'

def put_method(username, birthdate):
    r = requests.put(url + '/' + username, json={"dateOfBirth": birthdate})
    return int(r.status_code)

def get_method(username):
    r = requests.get(url + '/' + username)
    return r.text

def test_put_common():
    assert put_method(put_common_data[0], put_common_data[1]) == 204

def test_put_wrong():
    assert put_method(put_wrong_data[0], put_wrong_data[1]) == 400

def test_put_today():
    assert put_method(put_today_data[0], put_today_data[1]) == 204

def test_get_common():
    today = datetime.date.today()
    next_bday = datetime.date(today.year, 9, 13)
    if today < next_bday:
        days = (next_bday - today).days
    else:
        next_bday = datetime.date(today.year + 1, 9, 13)
        days = (next_bday - today).days
    assert get_method(get_common_data) == '{"message": "Hello, %s! Your birthday is in %s day(s)!"}' % (get_common_data, days)

def test_get_wrong():
    assert get_method(get_wrong_data) == '404 Not Found'

def test_get_today():
    assert get_method(get_today_data) == '{"message": "Hello, %s! Happy birthday!"}' % (get_today_data)