import sys
input = lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
dic = {}
for i in range(1,n+1):
    dic[i] = []

for i in range(n-1):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

pli = [0]*(n+1)
vis = [False]*(n+1)
def fin(n):
    for i in dic[n]:
        if not vis[i] and i!=1:
            pli[i] = n
            vis[i] = True
            fin(i)
            vis[i] = False
fin(1)
print(*pli[2:n+1], sep='\n')#  제출 번호 : 80068733, 메모리 : 73112, 시간 : 384