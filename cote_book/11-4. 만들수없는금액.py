from itertools import combinations
n = int(input())
array = list(map(int, input().split()))
print(array)
combs = []

for i in range(1, n):
    cur = combinations(array, i)
    for j in cur:
        #print(sum(j))
        combs.append(sum(j))

combs.sort()
combs = set(combs)
print(combs)
combs = list(combs)

value = 1
while True:
    if value in combs:
        value += 1
    else:
        break
print(value)
