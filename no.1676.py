N = int(input())
S = 1
answer = 0

for i in range(N, 0, -1):
    S *= i

for i in str(S)[::-1]:
    if i == '0':
        answer += 1
    else:
        break
print(answer)