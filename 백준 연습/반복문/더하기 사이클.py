n = int(input())
dum = n
cycle = 0

while True :

    sum = n % 10 + n // 10
    new = n % 10 * 10 + sum % 10
    n = new
    cycle += 1

    if dum == n :
        print(cycle)
        break
