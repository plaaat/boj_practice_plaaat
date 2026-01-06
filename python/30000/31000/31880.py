import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
sn = sum(map(int,input().split()))
mli = list(map(int,input().split()))

for x in mli:
    if x != 0:
        sn *= x

print(sn)

# 제출 번호 : 101589923, 메모리 : 32412, 시간 : 36