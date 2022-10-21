arr = [0] * 10

for i in range(10) :
    arr[i] = int(input())
    arr[i] = arr[i] % 42

set1 = set(arr)
n = len(set1)

print(n)