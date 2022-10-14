
# 입력값
n = str(input())
num = len(n)
m = int(n)

a = num // 2
hap_0 = 0
hap_1 = 0

for i in range(0, a) :
    hap_0 += int(n[i])

for j in range(a, num) :
    hap_1 += int(n[j])

if hap_0 == hap_1 :
    print("LUCKY")
else :
    print("READY")