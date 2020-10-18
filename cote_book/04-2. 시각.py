n = int(input())
result = 0
value = [3, 13, 23]

for i in range(0, n+1):
    print(i)
    if i in value:
        result += 3600
    else:
        result += 1575
print(result)
