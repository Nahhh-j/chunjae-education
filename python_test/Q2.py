'''
[Question 2] = (20점)
한 반 학생들의 이름과 수학 점수가 담긴 2차원 리스트가 주어질 때, ex) [이름, 점수]
수학 점수가 가장 높은 사람의 이름을 출력하시오.
'''

scores = [['alex', 30], ['rachel', 25], ['fred', 50], ['june', 80],
          ['jane', 90], ['elle', 40], ['ken', 65], ['jun', 85],
          ['chelsea', 60], ['gorden', 75], ['kelly', 100], ['kate', 55],
          ['jacob', 15], ['harry', 70], ['haley', 55], ['kyle', 95]]

highest_score_name = ''
highest_score = 0

for student in scores:
    if student[1] > highest_score:
        highest_score = student[1]
        highest_score_name = student[0]

print(highest_score_name)