array = [int(i) for i in input()]
print(array)

cur = array[0]
count = 0
for i in array:
    if i != cur:
        count += 1
        cur = i
result = (count+1)//2
print(result)