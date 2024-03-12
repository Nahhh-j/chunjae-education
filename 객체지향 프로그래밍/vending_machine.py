# python 복습

'''
다음과 같은 데이터가 주어져있을 때, 음료수 자판기를 사용자가 사용하는 시나리오까지 포함하여 구현하시오.

[음료, 가격, 재고]

시나리오:
1. 프로그램을 실행하면 자판기가 시작됩니다.
2. 사용자에게 음료 목록이 표시됩니다. 각 음료의 이름, 가격, 재고가 표시됩니다.
3. 사용자는 음료 번호를 선택하여 구매할 수 있습니다.
4. 선택한 음료의 재고가 있는 경우 구매가 완료되고 재고가 감소합니다.
5. 선택한 음료의 재고가 없는 경우 품절 메시지가 표시됩니다.
6. 사용자가 'q'를 입력하여 종료할 때까지 프로그램은 계속 실행됩니다.
'''

class Beverage: #개별 음료의 정보
    def __init__(self, name, price, stock): #각 음료의 이름, 가격, 재고를 초기화
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self): #음료를 구매하는 메서드, 재고가 있는 경우 재고를 감소시키고 구매 완료 메시지를 출력
        if self.stock > 0:
            print("------------------------------")
            print(f"구매완료 : {self.name} (가격: {self.price}원)")
            self.stock -= 1
        else:
            print("------------------------------")
            print(f"{self.name}은(는) 품절되었습니다.")

class Machine: #클래스는 음료 자판기 전체
    def __init__(self): #자판기에 있는 음료들을 초기화
        self.beverage = [
            Beverage("사이다", 1300, 4),
            Beverage("콜라", 1500, 2),
            Beverage("생수", 900, 1)
        ]

    def Menu(self): #사용자에게 음료 목록을 표시
        print("------------------------------")
        print("음료 자판기 메뉴")
        for index, beverage in enumerate(self.beverage, start=1):
            print(f"{index}. {beverage.name} (가격: {beverage.price}원, 재고 {beverage.stock}개)")

    def select_beverage(self, choice): #사용자의 음료 선택을 처리한다. 선택이 유효한지 확인하고, 해당 음료의 `purchase` 메서드를 호출한다.
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.beverage):
                beverage = self.beverage[choice - 1]
                beverage.purchase()
            else:
                print("땡")

        except ValueError:
            print("숫자를 입력하세요")

    def run(self): #자판기를 실행하는 메서드, 사용자에게 메뉴를 표시하고 음료를 선택하고, 종료를 선택할 때까지 반복한다.
        print("자판기 start!")
        while True:
            self.Menu()
            choice = input("음료 번호를 선택하세요 (종료는 q를 입력) : ")
            if choice.lower() == 'q':
                print("------------------------------")
                print("음료 자판기 종료~~")
                break

            else:
                self.select_beverage(choice)

if __name__ == "__main__":
    machine = Machine()
    machine.run()