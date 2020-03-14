from requests import get, post, delete, patch

print(get('http://localhost:5000/api/v2/jobs').json())  # Успешно
print(get('http://localhost:5000/api/v2/jobs/1').json())  # Успешно
print(get('http://localhost:5000/api/v2/jobs/555').json())  # 'Job 555 not found'
print(post('http://localhost:5000/api/v2/jobs', json={
                'id': 3,
                'team_leader': 2,
                'job': 'doing good mood ^_^',
                'collaborators': '1, 2',
                'work_size': 50,
                'is_finished': True}).json())  # Успешно
print(post('http://localhost:5000/api/v2/jobs', json={
                'id': 4,
                'team_leader': 2,
                'is_finished': True}).json())  #

print(delete('http://localhost:5000/api/v2/jobs/st').json())  # Not found
print(delete('http://localhost:5000/api/v2/jobs/55').json())  # Job 55 not found
# print(delete('http://localhost:5000/api/v2/jobs/3').json())  # Успешно
print(get('http://localhost:5000/api/v2/jobs').json())  # Успешно

print(patch('http://localhost:5000/api/v2/jobs/2',
            json={
                'job': 'seminar: how to smile?!',
                'collaborators': '2, 5, 10'}).json())  # OK
print(patch('http://localhost:5000/api/v2/jobs').json())  # 'The method is not allowed for the requested URL.'
print(patch('http://localhost:5000/api/jobs/v2/kjdihv').json())  # Not found

# Для REST-API v1
# print(get('http://localhost:5000/api/jobs').json())  # Получение всех работ
# print(get('http://localhost:5000/api/jobs/1').json())  # Корректное получение одной работы
# print(get('http://localhost:5000/api/jobs/999').json())  # Ошибочный запрос на получение одной работы — неверный id
# print(get('http://localhost:5000/api/jobs/q').json())  # Ошибочный запрос на получение одной работы — строка

# print(post('http://localhost:5000/api/jobs',
#           json={'id': 10, 'job': 'installation of radiation protection'}).json())  # not full list of characters
# print(post('http://localhost:5000/api/jobs').json())  # empty request
# print(post('http://localhost:5000/api/jobs',
#            json={'id': 10, 'job': 'installing a long-distance communication antenna', 'team_leader': 1, 'work_size': 23,
#                  'collaborators': '6, 3, 8', 'is_finished': True}).json())  # cool request
# print(get('http://localhost:5000/api/jobs').json())

#
# print(delete('http://localhost:5000/api/jobs/555').json())  # Not found
# print(delete('http://localhost:5000/api/jobs/kdhfjh').json())  # Not found
# print(delete('http://localhost:5000/api/jobs/10').json())
# print(get('http://localhost:5000/api/jobs').json())

# print(get('http://localhost:5000/api/v2/users').json())  # Успешно
# print(get('http://localhost:5000/api/v2/users/1').json())  # Успешно
# print(get('http://localhost:5000/api/v2/users/555').json())  # 'User 555 not found'
# print(post('http://localhost:5000/api/v2/users', json={
#                 'id': 3,
#                 'surname': 'Felay',
#                 'name': 'Bob',
#                 'age': 55,
#                 'position': 'marsolet',
#                 'speciality': 'engineer',
#                 'address': 'module_5',
#                 'email': 'bob@mars.org',
#                 'hashed_password': 'bob'}).json())  # Успешно
# print(post('http://localhost:5000/api/v2/users', json={
#                 'id': 4,
#                 'surname': 'New',
#                 'name': 'Bobby',
#                 'age': 15,
#                 'position': 'marsolet',
#                 'speciality': 'engineer',
#                 'address': 'module_3'}).json())  # {'email':
#                                                  # 'Missing required parameter in the JSON body
#                                                  # or the post body or the query string'}}
#
# print(delete('http://localhost:5000/api/v2/users/st').json())  # Not found
# print(delete('http://localhost:5000/api/v2/users/55').json())  # 'User 55 not found'
# print(delete('http://localhost:5000/api/v2/users/3').json())  # Успешно
# print(get('http://localhost:5000/api/v2/users').json())  # Успешно

# print(patch('http://localhost:5000/api/jobs/2',
#             json={
#                 'id': 2,
#                 'job': 'jobbbb',
#                 'collaborators': '2, 3'}).json())  # OK
# print(patch('http://localhost:5000/api/jobs/2').json())  # Empty request
# print(patch('http://localhost:5000/api/jobs/kjdihv').json())  # Not found
# print(get('http://localhost:5000/api/jobs').json())




