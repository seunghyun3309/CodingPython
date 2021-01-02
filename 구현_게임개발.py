n, m = map(int, input().split())
a, b, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
array2 = []
visited = [[0] * m for _ in range(n)]  # 2차원 배열 False로 초기화
for row in range(n):
    array2.append(list(map(int, input().split())))  # 고차원 배열을 받을 때 사용!

# d=(d+3)%4 <=(d-1)%4

xpos, ypos = a, b
visited[xpos][ypos] = True
turn_time = 0
while True:
    d = (d + 3) % 4  # 반시계방향으로 이동
    turn_time += 1
    nx = a + dx[d]  # x의 움직임
    ny = b + dy[d]  # y의 움직임
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    elif (visited[nx][ny] == 0) and (array2[nx][ny] == 0):  # 방문 안한 곳
        visited[nx][ny] = 1
        a = nx
        b = ny
        turn_time = 0
        cnt += 1
    if turn_time == 4:
        turn_time = 0

        if array2[a - dx[d]][b - dy[d]] == 0:
            a -= dx[d]
            b -= dy[d]
        else:
            break;

print(cnt)
