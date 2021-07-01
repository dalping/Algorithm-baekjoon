
def cut(graph, n):

    if len(graph)

    for k in range(n):
        for i in range(3 * k, 3 * k + 3):
            for j in range(3 * k, 3 * k + 3):

N = int(input())
graph = []
d = dict()
d[-1], d[0], d[1] = 0, 0, 0
paper = {-1, 0, 1}

for _ in range(N):
    graph.append(list(map(int, input().split())))

if cut(graph) == True:
    print(d[-1])
    print(d[0])
    print(d[1])

else:
    N = N / 3
    for k in range():
        for i in range():
            for j in range():



