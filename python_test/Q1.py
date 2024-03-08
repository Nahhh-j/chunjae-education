'''
[Question 1] = (10점)
빈 nums 리스트가 주어질 때, 1부터 30 까지의 숫자 중
2의 배수도 아니고 3의 배수도 아닌 수를 모두 모은 후,
nums 리스트의 길이를 출력하시오.
ex) [1, 5, 7, 11, 13, 17, 19, 23, 25, 29] => 10개
'''

nums = []

for i in range(1, 31):
    if i % 2 != 0 and i % 3 != 0:
        nums.append(i)

print(len(nums))