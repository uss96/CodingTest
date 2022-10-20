t = int(input())

for i in range(t) :
    a, b = map(int, input().split())
    c = a + b
    print("Case #" + str(i + 1) + ": " + str(c))