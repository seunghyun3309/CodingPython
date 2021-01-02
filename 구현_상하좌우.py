n = int(input())  # 지도의 크기

loc = input().split()  # 움직임을 입력 받음

xpos = 1
ypos = 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_dir = ['R', 'U', 'L', 'D']

for move in loc:
    for i in range(len(move_dir)):
        if move == move_dir[i]:
            xpos += dx[i]
            ypos += dy[i]
        if xpos < 1 or xpos > n or ypos < 1 or ypos > n:  # 범위를 벗어난 경우
            xpos -= dx[i]
            ypos -= dy[i]

print(xpos, ypos)
