n, m = map(int, input().split())
array = list(input().split())

cur1 = 0
cur2 = 0
count = 0

for i in range(0, n):
    cur1 = array[i]
    for j in range(i+1, n):
        if cur1 != array[j]:
            count += 1

print(count)