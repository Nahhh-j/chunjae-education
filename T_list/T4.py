# 전체 리스트에서, 연속한 3개짜리 구간(1)
def find_max_sum(lst):
    max_sum = float('-inf') 
    max_mean = 0

    # 리스트를 순회하면서 연속한 3개의 구간의 합을 계산
    for i in range(len(lst) - 2):
        current_sum = sum(lst[i:i+3])  
        if current_sum > max_sum:  
            max_sum = current_sum
            max_mean = lst[i:i+3]  
    return max_mean

num = [1, 7, 2, 8, 9, 7, 4, 5, 11, 1]
max_mean = find_max_sum(num)

print("최대 합을 가진 연속한 3개의 구간:", max_mean)

# 전체 리스트에서, 연속한 3개짜리 구간(2)
def find_max_sum(lst):
    n = len(lst)
    max_sum = float('-inf')
    max_triplet = None

    sums = [sum(lst[:3])]

    for i in range(1, n - 2):
        sums.append(sums[-1] - lst[i - 1] + lst[i + 2])

    max_sum_index = sums.index(max(sums))
    max_triplet = lst[max_sum_index:max_sum_index + 3]
    max_sum = sums[max_sum_index]

    return max_triplet

num = [1, 7, 2, 8, 9, 7, 4, 5, 11, 1]
max_triplet = find_max_sum(num)

print("최대 합을 가진 연속한 3개의 구간:", max_triplet)