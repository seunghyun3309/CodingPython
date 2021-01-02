N, K = map(int, input().split())

cnt = 0
while (N > 1):
    if N % K == 0:
        N //= K
        cnt += 1
    else:
        div = N % K
        N -= div
        cnt += div
print(cnt)
