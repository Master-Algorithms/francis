size = int(input())
plan = input().split()
length = len(plan)
print(plan)
# L, R, U, D
dx = [0, 0, -1, 1]  #행
dy = [-1, 1, 0, 0]  #열
x = 1
y = 1
for i in range(length):
    index = plan[i]
    if index == 'L' and y >= 2:
        x += dx[0]
        y += dy[0]
    elif index == 'R' and x < size:
        x += dx[1]
        y += dy[1]
    elif index == 'U' and x >= 2:
        x += dx[2]
        y += dy[2]
    elif index == 'D' and y < size:
        x += dx[3]
        y += dy[3]
    else:
        continue

print(x, y)
