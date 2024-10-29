import sys
from itertools import product
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(m)]

for tf in product([0,1],repeat=n):
    for a,b in li:
        if a < 0 and b < 0:
            a = (0 if tf[abs(a)-1] else 1)
            b = (0 if tf[abs(b)-1] else 1)
        elif a < 0:
            a = (0 if tf[abs(a)-1] else 1)
            b = tf[abs(b)-1]
        elif b < 0:
            b = (0 if tf[abs(b)-1] else 1)
            a = tf[abs(a)-1]
        else:
            a = tf[abs(a)-1]
            b = tf[abs(b)-1]
        if not a and not b:
            break
    else:
        print(1)
        print(*tf)
        break
else:
    print(0)
    
# 제출 번호 : 85695943, 메모리 : 31120, 시간 : 2020