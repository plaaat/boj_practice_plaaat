import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

nli = [0] + [i for i in range(1,n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    nli[i], nli[j] = nli[j], nli[i]

print(*nli[1:])