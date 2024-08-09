import sys

input = lambda: sys.stdin.readline().rstrip()

a,b,c,m = map(int,input().split())
num = 0
pn = 0

for _ in range(24):
    if pn+a > m:
        if pn < c:
            pn = 0
        else:
            pn -= c
        continue
    
    pn += a
    num += b

print(num)


# 제출 번호 : 82248747 메모리 : 31120 시간 : 32