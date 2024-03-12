# 실습2

'''
다음 시나리오를 바탕으로 자유롭게 구현하시오.
간단한 사냥게임을 구현합니다.
사냥꾼은 무기를 활용하여 동물을 사냥합니다.
무기의 종류는 총, 검 두개(또는 그 이상)이며, 각각 상이한 공격력을 가지고 있습니다.
사냥감은 괴물이며, 괴물은 사냥꾼에게 공격당하면 체력을 소모합니다.
체력을 모두 소모하면 괴물은 괴성을 지르며 사라집니다.

시나리오:
1. 게임이 시작되면, 사용자에게 괴물의 체력이 표시됩니다.
2. 사용자는 총 또는 검 중 하나를 선택하여 괴물을 공격할 수 있습니다.
3. 선택한 무기에 따라 무기의 공격력이 적용됩니다.
4. 괴물이 공격을 받으면 해당 무기의 공격력에 따라 괴물의 체력이 감소합니다.
5. 괴물의 체력이 0 이하가 되면 괴물은 사라지고 게임이 종료됩니다.
'''

import random

class Hunter:
    def __init__(self, name):
        self.name = name
        self.weapons = []
    
    def add_weapon(self, weapon):
        self.weapons.append(weapon)
    
    def attack(self, monster):
        if not self.weapons:
            print("사냥꾼은 무기를 가지고 있지 않습니다!")
            return
        weapon = random.choice(self.weapons)
        print(f"{self.name}이(가) {weapon.name}으로 공격합니다!")
        monster.take_damage(weapon.damage)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}이(가) {damage}의 피해를 입었습니다!")
        if self.health <= 0:
            print(f"{self.name}이(가) 죽었습니다! {self.name}의 괴성이 들렸습니다!")
            del self

# 무기 생성
gun = Weapon("총", 30)
sword = Weapon("검", 20)

# 사냥꾼 생성
hunter = Hunter("용사")
hunter.add_weapon(gun)
hunter.add_weapon(sword)

# 괴물 생성
monster = Monster("괴물", 100)

print("사냥 게임을 시작합니다!")
while monster.health > 0:
    print("------------------------------")
    print(f"{monster.name}의 체력: {monster.health}")
    print("무기 선택: 1. 총, 2. 검")
    choice = input("무기를 선택하세요: ")
    if choice == '1':
        hunter.attack(monster)
    elif choice == '2':
        hunter.attack(monster)
    else:
        print("올바른 번호를 입력하세요!")

print("게임 종료!")