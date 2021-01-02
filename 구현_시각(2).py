n = int(input()) # 문자->int형으로 변환하여 입력을 받음
h ,m, s = 0, 0, 0
result = 0
for h in range(n+1): # 0~n까지
   for m in range(60):
       for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                result+=1
print(result)
