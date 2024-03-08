def generate_lotto_numbers(name):
    # 이름을 거꾸로 뒤집기
    reversed_name = name[::-1]
    
    # 각 글자에 대해 특정한 숫자를 할당하여 로또 번호 생성
    lotto_numbers = []
    for char in reversed_name:
        # ASCII 코드 값을 이용하여 각 글자에 대해 특정 숫자 생성
        number = ord(char) % 45 + 1
        # 생성된 숫자가 중복되지 않도록 처리
        while number in lotto_numbers:
            number = (number + 1) % 45 + 1
        lotto_numbers.append(number)
    
    return sorted(lotto_numbers)

# 사용자로부터 이름 입력 받기
name = input("이름을 입력하세요: ")

# 로또 번호 생성 및 출력
lotto_numbers = generate_lotto_numbers(name)
print(name + "님의 로또 번호는", lotto_numbers, "입니다.")
