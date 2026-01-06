import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
nli = list(map(int,input().split()))
res = sum(nli[:m])
tres = res
for i in range(m,n):
    tres = nli[i] + tres - nli[i-m]
    res = max(res, tres)

print(res)

# 제출 번호 : 101662638, 메모리 : 42700, 시간 : 84