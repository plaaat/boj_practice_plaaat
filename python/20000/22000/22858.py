import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())
sli = list(map(int,input().split()))
dli = list(map(int,input().split()))

for _ in range(k):
    tli = [0 for _ in range(n)]
    for i in range(n):
        tli[dli[i]-1] = sli[i]
    sli = tli

print(*sli)

# 제출 번호 : 84519334, 메모리 : 32140, 시간 : 1344