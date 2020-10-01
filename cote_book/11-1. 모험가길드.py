<<<<<<< HEAD
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

=======
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

>>>>>>> 033258224181217757944f3e21cf4c9dbb5db85e
print(group)