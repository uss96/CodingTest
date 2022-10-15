# 입력값 받기

n = str(input())

answer = len(n)

for i in range(1, len(n) // 2 + 1) :
    compress = ""
    prev = n[0:i] # 앞에서부터 i만큼 문자열 추출
    count = 1

    # 단위 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(i, len(n), i) :
        # 이전 상태와 동일하다면 압축 횟수 증가
        if prev == n[j : j + i] :
            count += 1
        # 다른 문자열이 나왔다면 (더 이상 압축 X)
        else :
            if count >= 2 :
                compress += str(count) + prev
            else :
                compress += prev
            prev = n[j : j + i] # 다시 상태 초기화
            count = 1

    # 남아 있는 문자열에 대해 처리
    if count >= 2 :
        compress += str(count) + prev
    else :
        compress += prev

    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compress))

print(answer)
