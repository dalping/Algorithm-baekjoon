arr2 = [[0,0,0],[1,1,1]]
arr1 = []

arr1 = arr2[:]

arr1[0][0] = 10

print(arr2[0][0])