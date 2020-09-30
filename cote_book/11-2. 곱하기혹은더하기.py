s = input()
array = [int(i) for i in s]    #***** string 하나씩 split 방법
print(array)
result = array[0]

for i in range(1, len(array)):
    if result <= 1 or i <= 1:
        result += i
    else:
        result *= i

print(result)
