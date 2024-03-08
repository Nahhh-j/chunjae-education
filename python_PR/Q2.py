# 입력된 문자열을 뒤집은 문자열을 구하시오.
# ex) banana 입력 시 ananab 출력
word = input()

# 풀이 1
reversed_word = word[::-1]  # 문자열 전체 슬라이싱 후 반대로 뒤집기
print(reversed_word)

# 풀이 2
reversed_word = ''  # 빈 스트링을 1개 초기화하고
for w in word:  # 반복문을 쭉 돌면서
    reversed_word = w + reversed_word  # w를 앞에 두고 앞에서부터 거꾸로 붙여 나간다.
print(reversed_word)

# 풀이 3
str_list = list(word)  # 리스트로 형변환 하고 == ['b', 'a', 'n', 'a', 'n', 'a']
str_list.reverse()  # '리스트 메서드'를 사용해서 뒤집고 == ['a', 'n', 'a', 'n', 'a', 'b']
reversed_word = ''.join(str_list)  # 빈 문자열로 남김없이 붙여버리면!
print(reversed_word)  # 완성