# <절댓값 구하기>
# A와 B 정수를 입력받아 두 수의 차의 절댓값을 반환하는 함수를 만드시오.
# 만약 7과 -3을 받았다면 10을 출력해야 한다.

A = int(input())
B = int(input())

def get_absolute_value(x, y):
    diff = x - y
    if diff >= 0:
        return diff
    else:
        return -diff

print(get_absolute_value(A, B))