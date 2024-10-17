import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = abs(int(input()))
now = 1

if n == 0:
    print(0)
elif n % 2 == 0:
    print(-1)
else:
    pn = 0
    while n > 0:
        n //= 2
        now *= (now * 2) - 1
        pn += 1
    print(pn)
    
# 제출 번호 : 85136014, 메모리 : 34000, 시간 : 52