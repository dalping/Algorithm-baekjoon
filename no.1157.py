s = input().upper()

d = dict()

for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1

M = max(d.values())
if list(d.values()).count(M) > 1:
    print('?')
else:
    for i in d.keys():
        if d[i] == M:
            print(i)