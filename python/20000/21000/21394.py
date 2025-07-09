import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    inp = list(map(int,input().split()))
    inp[8] += inp[5]
    inp[5] = 0
    ln = sum(inp)
    nli = [0] * ln
    ln -= 1
    fla = True
    n = 9
    ind = 0
    while inp:
        x = inp.pop()
        for _ in range(x):
            if fla:
                nli[ind] = n
                fla = False
            else:
                nli[ln - ind] = n
                ind += 1
                fla = True
        n -= 1
    print(*nli)

# 제출 번호 : 96102981, 메모리 : 32412, 시간 : 56