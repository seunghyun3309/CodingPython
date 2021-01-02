# 가장 큰수 * K + 두번째 큰 수 반복하다가 M되면 stop

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1] # 첫번째로 큰 수
second = data[n-2] # 두번째로 큰 수

cycle = first * k + second

result = cycle * (m // (k+1)) + first * (m % (k+1))
print(result)
