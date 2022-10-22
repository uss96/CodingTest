def solve(a : list) -> int :
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans
