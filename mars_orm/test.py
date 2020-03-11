from requests import get, post

# print(get('http://localhost:5000/api/jobs').json())  # Получение всех работ
# print(get('http://localhost:5000/api/jobs/1').json())  # Корректное получение одной работы
# print(get('http://localhost:5000/api/jobs/999').json())  # Ошибочный запрос на получение одной работы — неверный id
# print(get('http://localhost:5000/api/jobs/q').json())  # Ошибочный запрос на получение одной работы — строка

print(post('http://localhost:5000/api/jobs',
          json={'id': 10, 'job': 'installation of radiation protection'}).json())  # not full list of characters
print(post('http://localhost:5000/api/jobs').json())  # empty request
print(post('http://localhost:5000/api/jobs',
           json={'id': 10, 'job': 'installing a long-distance communication antenna', 'team_leader': 1, 'work_size': 23,
                 'collaborators': '6, 3, 8', 'is_finished': True}).json())  # cool request
print(get('http://localhost:5000/api/jobs').json())
