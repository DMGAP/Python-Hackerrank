n = int(input())
arr = list(map(int, input().strip().split()))
x = max(arr)

for i in range(n):
    if x == max(arr):
        arr.remove(x)

print(max(arr))
