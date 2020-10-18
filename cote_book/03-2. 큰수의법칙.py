n, m, k = map(int, input().split())
array = [int(i) for i in input().split()]
#print(array)
array.sort(reverse=True)
print(array)

total = 0
cur = 0
for i in range(m):
    if cur < k:
        total += array[0]
        cur += 1
        print(i, total)
    else:
        total += array[1]
        cur = 0
        print(i, total)
print(total)
