import sys
input = lambda: sys.stdin.readline().rstrip()

x,y,px,py = map(int,input().split())

p = px
mp = max(px, py)
while True:
    if p >= py and (p - py) % y == 0:
        print(p)
        break
    p += x
    if p > x * y + mp:
        print(-1)
        break

# 제출번호 : 101216973, 메모리 : 32412, 시간 : 36