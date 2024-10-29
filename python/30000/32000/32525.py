import sys
from random import randint
input = lambda: sys.stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) > 0

def chk(x1, y1, x2, y2, x3, y3, x4, y4):
    return (ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4) and 
            ccw(x3, y3, x4, y4, x1, y1) != ccw(x3, y3, x4, y4, x2, y2))

t = int(input())
for _ in range(t):
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]
    
    pli = []
    
    while len(pli) < n:
        x, y = randint(- 10 ** 9, 10 ** 9), randint(- 10 ** 9, 10 ** 9)
        
        tvis = [(li[i][0], li[i][1], pli[i][0], pli[i][1]) for i in range(len(pli))]
        now = (li[len(pli)][0], li[len(pli)][1], x, y)
        
        for i in tvis:
            if chk(*i, *now):
                break
        else:
            pli.append((x, y))
            continue
            
    for i in range(1, len(pli) + 1):
        x, y = pli[i-1]
        print(i, x, y)