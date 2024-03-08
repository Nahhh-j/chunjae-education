# 첫 번째 문제: 평균 나이 계산 함수
def calculate_average_age(user_info):
    total_age = sum(user['age'] for user in user_info['information'])
    num_users = len(user_info['information'])
    average_age = total_age / num_users
    return average_age

# 두 번째 문제: 면허 보유자 수 계산 함수
def count_license_holders(user_info):
    license_holders = sum(1 for user in user_info['information'] if user['license'])
    return license_holders

# 주어진 사용자 정보
users = {
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}

users2 = {
    'information': [
        {'name': 'elle', 'age': 9, 'license': True},
        {'name': 'josh', 'age': 3, 'license': False},
        {'name': 'harry', 'age': 1, 'license': False},
        {'name': 'ken', 'age': 5, 'license': True},
        {'name': 'jane', 'age': 2, 'license': True},
        {'name': 'ellisa', 'age': 8, 'license': True}
    ]
}

# 테스트 및 결과 출력
print(f"첫 번째 사용자 그룹의 평균 나이: {calculate_average_age(users)}")
print(f"두 번째 사용자 그룹의 평균 나이: {calculate_average_age(users2)}")

print(f"첫 번째 사용자 그룹의 면허 보유자 수: {count_license_holders(users)}")
print(f"두 번째 사용자 그룹의 면허 보유자 수: {count_license_holders(users2)}")