import sys
input = lambda:sys.stdin.readline().rstrip()

def bubble_sort(arr,n,m):
    num = 0
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num+=1
                swapped = True
            if num == m:
                print(*arr)
                return
        if not swapped:
            break
    if not swapped:
        print(-1)
n,m = map(int,input().split())
li = list(map(int,input().split()))
bubble_sort(li,n,m)

#pypy3