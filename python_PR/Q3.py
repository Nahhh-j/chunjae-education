# 주어진 배열 안의 값을 전부 2배로 만드시오.
# ex) [7, 2, 3]의 경우 [14, 4, 6]이 되어야 합니다.
nums = [7, 2, 9, 8, 4, 3, 5]

# 풀이 1 (다른 리스트로 만들기)
double_nums = []  # 빈 리스트를 만들고
for num in nums:  # 반복문을 돌면서
    double_nums.append(num*2)  # 2배 값을 계산한 후 더해준다!

print(double_nums)

# 풀이 2 (원본을 수정하기)
for i in range(len(nums)):  # 인덱스 번호로 접근해서
    # nums[i] = nums[i] * 2
    nums[i] *= 2  # 2배 처리를 하여 해당 원소값을 수정한다.
print(nums)