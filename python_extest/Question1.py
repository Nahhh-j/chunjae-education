'''
[Question 1] = (10점)
nums 리스트가 주어질 때, 주어진 리스트의 원소 중
5를 포함한 5의 배수들의 전체 합산을 구하시오.
'''

nums = [5, 1, 4, 10, 2, 15, 7, 5, 30, 8, 6, 17]
answer = 0  # 답을 모아줄 변수 초기화

for num in nums:  # nums 리스트를 반복
    if num % 5 == 0:  # 만약 5의 배수라면?
        answer += num  # 답 변수에 집계
print(answer)  # 65가 출력되어야 합니다.