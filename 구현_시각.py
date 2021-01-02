n = int(input())  # 문자->int형으로 변환하여 입력을 받음
h, m, s = 0, 0, 0
result = 0
while (h <= n):  # N보다 커지면 종료
    flag = False
    if s == 59 and m == 59:  # h변경 조건
        h += 1
        s = 0
        m = 0
    elif s == 59:  # m 변경 조건
        m += 1
        s = 0
    else:  # s 변경 조건
        s += 1
    # str = str(h)+str(m)+str(s)
    if '3' in str(h) + str(m) + str(s):
        result += 1
print(result)
