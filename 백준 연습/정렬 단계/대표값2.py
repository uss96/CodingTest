arr = []
count= 0
for i in range(5):
    a = int(input())
    arr.append(a)
    count += a

print(int(count/5))
arr.sort()
print(arr[2])