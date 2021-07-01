N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

tmp = [0 ,0 ,0]
answer = 0

for a in range(len(arr)):
    tmp[0] = arr[a]
    for b in range(len(arr)):
        if b != a:
            tmp[1] = arr[b]
        for c in range(len(arr)):
            if c != a and c != b:
                tmp[2] = arr[c]
                s = sum(tmp)
                if s <= M and answer < s:
                    answer = s

print(answer)

