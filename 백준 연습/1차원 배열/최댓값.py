arr = [0] * 9

for i in range (9) :
    arr[i] = int(input())

c = max(arr)
print(c)

for i in range(9) :
    if arr[i] == c :
        print(i+1)
