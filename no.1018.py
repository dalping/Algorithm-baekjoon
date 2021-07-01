from collections import deque

def BFS(graph, target):
    G = graph
    count = 0
    queue = deque()
    queue.append((0, 0))

    if G[0][0] != target:
        count += 1
        G[0][0] = target

    while queue:

        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if G[x][y] == G[nx][ny]:
                count += 1
                if G[x][y] == 'W':
                    G[nx][ny] = 'B'
                else:
                    G[nx][ny] = 'W'

            queue.append((nx, ny))

    print(graph)

    return count

N, M = list(map(int, input().split()))
graph = []
#우측,하단
dx = [1, 0]
dy = [0, 1]

for i in range(N):
    graph.append(list(input()))

print(min(BFS(graph, 'W'), BFS(graph, 'B')))

