n = int(input())
list = [int(i) for i in input().split()]
print(list)
list = sorted(list)
print(list)
group = 0
cur = 0

for i in list:
    cur += 1
    if cur >= i:
        group += 1
        cur = 0

print(group)