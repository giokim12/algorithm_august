arr = [[1, 5, 3],
       [4, 5, 5],
       [3, 3, 5],
       [4, 6, 2]]

a, b = map(int, input().split())

for i in range(4):
    for j in range(3):
        if a<= arr[i][j] <=b:
            arr[i][j] = '#'


for s in range(4):
    for t in range(3):
        print(arr[s][t], end=' ')
    print()
