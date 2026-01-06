import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int, input().split())
nli = [sorted(list(map(int,input().split()))) for _ in range(n)]
dl = [0] * n
mxn = -1
mxli = []
mxan = 0
ans = []

for i in range(m):
    for j in range(n):
        if nli[j][m-i-1] > mxn:
            mxn = nli[j][m-i-1]
            mxli = [j]
        elif nli[j][m-i-1] == mxn:
            mxli.append(j)
    
    for j in mxli:
        dl[j] += 1
        mxan = max(mxan, dl[j])
    mxn = 0

for i in range(n):
    if dl[i] == mxan:
        ans.append(i+1)

print(*ans)

# 제출 번호 : 101592671, 메모리 : 32412, 시간 : 36