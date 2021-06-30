s = input()
answer = [-1] * 26
tmp = []

for i,j in enumerate(s):
    if j in tmp:
        continue

    answer[ord(j)-97] = i
    tmp.append(j)

print(' '.join(list(map(str, answer))))