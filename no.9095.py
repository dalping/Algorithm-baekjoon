T = int(input())
for i in range(T):
    V = int(input())
    arr = [0 for i in range(12)]
    arr[1], arr[2], arr[3] = 1, 2, 4

    if V > 3:
        for i in range(4, V + 1):
            arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

    print(arr[V])