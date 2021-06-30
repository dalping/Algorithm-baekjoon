A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
answer = [0] * 10

for i in result:
    answer[int(i)] += 1

for j in answer:
    print(j)