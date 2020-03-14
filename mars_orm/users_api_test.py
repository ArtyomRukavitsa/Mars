from requests import get, post, delete, patch

# Для REST-API v1
print(get('http://localhost:5000/api/users').json())  # Получение всех работ
print(get('http://localhost:5000/api/users/1').json())  # Корректное получение одной работы
print(get('http://localhost:5000/api/users/999').json())  # Ошибочный запрос на получение одной работы — неверный id
print(get('http://localhost:5000/api/users/q').json())  # Ошибочный запрос на получение одной работы — строка

print(post('http://localhost:5000/api/users', json={
    'id': 10,
    'name': 'Petr'}).json())  # not full list of characters
print(post('http://localhost:5000/api/users').json())  # empty request
print(post('http://localhost:5000/api/users',
           json={
               'id': 4,
               'surname': 'Miller',
               'name': 'Jerry',
               'age': 45,
               'position': 'historian',
               'speciality': 'mars guide',
               'address': 'module_2',
               'email': 'jerry_miller@mars.org',
               'hashed_password': 'jerry',
               'city_from': 'London'}).json())  # cool request
print(get('http://localhost:5000/api/users/4').json())

print(delete('http://localhost:5000/api/users/4').json())

print(patch('http://localhost:5000/api/users/3',
            json={
                'id': 3,
                'name': 'Marina'}).json())
