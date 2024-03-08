# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]

mean = sum(nums) / len(nums)  # 합산에서 길이를 나누면 평균!
answer = int(mean)
print(answer)  # 소숫점을 제외하기 위해 float 값을 int값으로 형변환 한다.
