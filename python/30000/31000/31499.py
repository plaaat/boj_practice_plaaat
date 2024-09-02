import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split())
pn = 1
if n == 1 and m == 1:
    pn = 0
for i in range(2,n+1):
    pn = (pn * i) % m
print(pn)

# 제출 번호 : 83329356, 메모리 : 31120, 시간 : 36