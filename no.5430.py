import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for c in range(T):
    p = list(input().rstrip())
    n = int(input())
    s = input().rstrip()
    reverse = False
    if s == '[]':
        arr = deque([])
    else:
        arr = deque(list(map(int, s[1: -1].split(','))))

    for i in p:
        if i == 'R':
            if reverse == True:
                reverse = False
            else:
                reverse = True
        else:
            if len(arr) == 0:
                print("error")
                break

            if reverse == False:
                arr.popleft()
            else:
                arr.pop()

    else:
        arr = list(map(str, [i for i in arr]))
        if reverse == False:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')