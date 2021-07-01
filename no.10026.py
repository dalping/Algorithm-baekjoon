from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

def DFS(x, y, target):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False

    if graph[x][y] == 'W':
        return False

    if graph[x][y] in target:
        graph[x][y] = 'W'
        DFS(x + 1, y, target)
        DFS(x - 1, y, target)
        DFS(x, y + 1, target)
        DFS(x, y - 1, target)
        return True
    return False

N = int(input())
graph = []
graph_tmp = []
answer1, answer2 = 0, 0
flag = 1

for _ in range(N):
    graph.append(list(input()))
graph_tmp = deepcopy(graph) #원본그래프 복사

for k in range(2):
    for i in range(N):
        for j in range(N):
            if graph[i][j] in {'R' ,'G' ,'B'}:
                if flag == 1: #적록색약이 아닌 경우
                    DFS(i, j, {graph[i][j]})
                    answer1 += 1
                else: #적록 색약인 경우
                    if graph[i][j] in {'R', 'G'}:
                        DFS(i, j, {'R', 'G'})
                    else:
                        DFS(i, j, {'B'})
                    answer2 += 1
    flag = 0
    graph = deepcopy(graph_tmp)

print(answer1, answer2)


