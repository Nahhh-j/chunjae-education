'''
[Question 2] = (20점)
각 후보의 투표 결과가 다음과 같을 때, 투표 결과를 집계하고,
그 중 가장 많은 표를 득표한 후보가 몇 표를 얻었는지 구하시오.
단, 후보는 A, B, C 세사람만 있다고 가정합니다.
ex) votes = ['B', 'B', 'C', 'C', 'A']일 때, 집계 결과는 {"A": 1, "B": 2, "C": 2}이며,
가장 많은 표를 득표한 후보의 표 수는 2표이다. (B 후보와 C 후보는 동률)
'''

votes = ["A", "C", "B", "B", "C", "A", "A", "B", "A", "C", "C", "A", "C", "A"]
results = {"A": 0, "B": 0, "C": 0}

for vote in votes:
    results[vote] += 1

# max_vote = 0
# for i in results.values():
#     if max_vote < i:
#         max_vote = i
# print(max_vote)

max_vote = max(results.values())
print(max_vote)