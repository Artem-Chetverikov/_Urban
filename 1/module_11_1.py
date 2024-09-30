import requests

# GET запрос:
print('GET запроc')
r = requests.get('https://www.python.org')
print(r.url)
print(r.status_code)
print('Python is a programming language' in r.text)
print(r.headers['Date'])

# POST запрос:
print('POST запрос')
payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

# работа с сессиями
print('работа с сессиями')
with requests.Session() as session:
    session.auth = ('chetverikov.av@mail.ru', input('Введите пароль: '))
    response = session.get('https://api.github.com/user')
print(response.headers)
print(response.json())
