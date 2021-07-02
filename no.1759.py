#암호는 사전순이며 최소 모음1개와 2개의 자음으로 구성된다.

def DFS(n, s, j, m):

    if len(s) > 0 and s[-1] > n: #사전순 아님
        return
    else:
        s += n
        if n in ('a','e','i','o','u'): #자음,모음 수
            m += 1
        else:
            j += 1

    if len(s) == L:
        if j >= 2 and m >= 1:
            answer.append(s)
        return

    for i in S:
        if i not in s:
            DFS(i, s, j, m)

L, C = list(map(int, input().split())) #자릿수, 알파벳 수
S = input().split()
answer = []

for i in S:
    DFS(i, '', 0, 0)

answer.sort()
for i in answer:
    print(i)

