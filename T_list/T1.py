# 전체 리스트에서, 연속한 3개짜리 구간을 모두 본다고 할 때, 그 합산이 최대가 되는 것을 구하여라
# 예를 들어 [1,7,2], [7,2,8], [2,8,9]...이렇게 반복한다.

def find_max_sum_of_triplet(lst):
    max_sum = float('-inf')  # 최대 합을 저장할 변수를 음의 무한대로 초기화합니다.
    max_triplet = None  # 최대 합을 가진 연속한 3개의 구간을 저장할 변수를 초기화합니다.

    # 리스트를 순회하면서 연속한 3개의 구간의 합을 계산합니다.
    for i in range(len(lst) - 2):
        current_sum = sum(lst[i:i+3])  # 현재 연속한 3개의 구간의 합을 계산합니다.
        if current_sum > max_sum:  # 현재 합이 최대 합보다 크다면
            max_sum = current_sum  # 최대 합을 갱신합니다.
            max_triplet = lst[i:i+3]  # 최대 합을 가진 연속한 3개의 구간을 저장합니다.

    return max_triplet

# 주어진 리스트에서 최대 합을 가진 연속한 3개의 구간을 찾습니다.
num = [1, 7, 2, 8, 9, 7, 4, 5, 11, 1]
max_triplet = find_max_sum_of_triplet(num)

print("최대 합을 가진 연속한 3개의 구간:", max_triplet)