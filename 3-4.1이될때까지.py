n, k = map(int, input().split())
result = 0

while n != 1:
    result += n % k
    n = n // k
    result += 1
print(result)
