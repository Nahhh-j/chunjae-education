# <미출석 인원 찾기>
# 전체 출석부와 현재 출석한 인원이 리스트로 주어질 때, 출석하지 않은 인원을 출력하시오. (순서 굳이 상관 없음)
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 전체 명단
attened = ['c', 'e', 'f', 'h']  # 출석 명단

# 풀이 1
for student in students:  # 전체 명단을 보면서
    if student not in attened:  # 만약 출석 명단에 없다면?
        print(student)  # 미출석 인원이므로 출력한다

# 풀이 2
students_set = set(students)  # 각각을 집합으로 만들고
attened_set = set(attened)
not_attened = students_set - attened_set  # A - B 집합 (차집합)을 구한다.
for student in not_attened:  # 해당 차집합에서 바로 뽑으면서 출력한다.
    print(student)
