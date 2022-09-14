m = int(input())#start
n = int(input())#end

arr = [True for i in range(n+1)]

for i in range(2, int(n**0.5 + 1)):
    if arr[i]:
        for j in range(2, n//i + 1):
            arr[i*j] = False

for i in range(m):
    arr[i] = False
arr[1] = False

lst = [i for i in range(n+1) if arr[i]]

# print(lst)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))