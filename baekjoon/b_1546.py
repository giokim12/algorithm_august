N = int(input())
arr = list(map(int, input().split()))
M = max(arr)

total = 0
for i in range(N):
    if arr[i]==M:
        total += arr[i]
    else:
        total += (arr[i]*100)/M

print(total/N)