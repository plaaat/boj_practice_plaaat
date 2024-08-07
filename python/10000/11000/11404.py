import sys
import heapq
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

li = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    li[a][b] = min(c,li[a][b])

for i in range(1,n+1):
    li[i][i] = 0

for i in range(1,n+1):
    for s in range(1,n+1):
        for j in range(1,n+1):
            li[s][j] = min(li[s][j],li[s][i]+li[i][j])

for i in li[1:]:
    for s in i[1:]:
        if s == float('inf'):
            print(0,end=' ')
        else:
            print(s,end=' ')
    print()


#  제출 번호 : 81038863, 메모리 : 33188, 시간 : 568