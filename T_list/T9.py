#(1)
votes = [1, 0, 1, 1, 2, 1, 0, 2, 1, 0, 2, 77]
result  = {}
for v in votes:
    if result.get(v, -1) == -1:
        result[v] = 1
    else:
        result[v] += 1

print(result)

#(2)
from collections import defaultdict

votes = [1, 0, 1, 1, 2, 1, 0, 2, 1, 0, 2, 77]

result = defaultdict(int)
for v in votes:
    result[v] += 1

print(dict(result))

#(3)
votes = [1, 0, 1, 1, 2, 1, 0, 2, 1, 0, 2, 77]
result  = {}
for v in votes:
    result[v] = result.get(v, 0) + 1
print(result)