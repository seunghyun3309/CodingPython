# 거스름돈
# /는 소수점까지 나오고 //는 소수점은 버림

n=int(input("N을 입력하세요 : "))
count=0

coin_types=[500,100,50,10]
for coin in coin_types: # coin 내에 배열 내에 있는 수를 0번부터 차례로 투입
    count += n // coin # 몫만큼 +
    n%=coin #  나머지 만큼 다시 시행

print(count)