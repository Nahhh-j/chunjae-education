money = int(input('가진 금액을 입력하세요 : '))
print('음료를 고르세요.')
choice = int(input('[1]요구르트(300원) [2]아메리카노(1000원) [3]초코우유(100원)'))

change = 0 
price = 0

if choice == 1:
    price = 300
elif choice == 2:
    price = 1000
elif choice == 3:
    price = 100

if money >= price:
    print('거스름돈: {}' .format(money - price))
else:
    print('money 부족!')