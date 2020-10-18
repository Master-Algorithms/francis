n = input()
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]
result = 0

for i in range(0, 8):
    if n[0] == column[i]:
        x = i + 1
y = int(n[1])

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    else:
        result += 1

print(result)
