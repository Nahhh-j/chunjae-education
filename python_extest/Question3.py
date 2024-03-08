'''
[Question 3] = (30점)
뒤집어도 같은 글자가 되는 단어를 '회문(palindrome)'이라고 정의할 때,
주어진 리스트에서 회문이 몇 개 있는지 고르는 함수를 완성하시오.
ex) 'box'를 뒤집으면 'xob'가 되므로 'box' != 'xob' 이다.
그런데, 'pop'을 뒤집으면 여전히 'pop'이 되므로 이것은 회문이다.
'''

words = ['banana', 'level', '역삼역', 'car', '별똥별', '우영우', 'palindrome']

def find_palindrome():
    cnt = 0  # 집계
    for word in words:  # 주어진 리스트를 돌면서
        if word == word[::-1]:  # 만약 원본과 뒤집은 스트링이 같다면?
            cnt += 1  # 집계 추가해주고
    return cnt  # 전체 집곗값을 반환한다.

answer = find_palindrome()
print(answer)