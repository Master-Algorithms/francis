n, m = map(int, input().split())
array = [[int(i) for i in input().split()] for j in range(n)]
print(array)
result = min(array[0])
print(array[1])

for i in range(1, n):
    cur = min(array[i])
    if cur > result:
        result = cur

print(result)
