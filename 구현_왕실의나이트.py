# 8x8 평면
input_data = input()
# xpos는 위아래 ypos는 좌우
xpos = int(input_data[1])
ypos = int(ord(input_data[0]))-int(ord('a'))+1 # 아스키코드는 ord

result = 0
nx, ny = xpos, ypos
# 나이트가 이동할 수 있는 방향
step = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
for st in step:
    nx = xpos+st[0]
    ny = ypos+st[1]
    if nx>=1 and nx<=8 and ny>=1 and ny<=8:
        result += 1

print(result)