# 가장 큰수 * K + 두번째 큰 수 반복하다가 M되면 stop

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 첫번째로 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0
count = 0
while True:
    for i in range(k):
        result+=first
        count+=1
        if count == m:
            break
    if count == m:
        break
    result+=second
    count += 1
    if count == m:
        break
print(result)
