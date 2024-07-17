import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nli = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    nli[a-1]+=1
    nli[b-1]+=1
print(*nli,sep = '\n')