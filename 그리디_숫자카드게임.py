n, m = map(int, input().split()) # n,m을 입력 받음
result = 0

for idx in range(n):
        data = list(map(int, input().split())) # 한 줄을 한번에 입력 받음
        min_line = min(data)
        if min_line > result:
            result = min_line

print(result)
