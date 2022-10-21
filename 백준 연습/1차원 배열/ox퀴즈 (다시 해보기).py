tc = int(input())
for i in range(tc) :
    ox = str(input())
    score = 0
    count = 0
    for j in list(ox) :
        if j == "O" :
            count += 1
            score += count
        elif j == "X" :
            count = 0
    print(score)
