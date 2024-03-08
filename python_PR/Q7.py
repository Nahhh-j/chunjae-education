# 다음과 같은 api 데이터가 있을 때, 모든 유저들의 이름을 모아보시오.
users = {
    'total_user': 3,
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}

names = []
for user in users['information']:
    names.append(user['name'])

print(names)  # ['alex', 'june', 'peter']