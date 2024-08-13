import sys

input = lambda: sys.stdin.readline().rstrip()

x,y = map(int,input().split())
li = []

for i in range(1,x*y+1):
    if i % x == 0 and i % y == 0:
        li.append(3)
    elif i % x == 0:
        li.append(2)
    elif i % y == 0:
        li.append(1)

print(*li,sep='')


# 제출 번호 : 82411004, 메모리 : 31120, 시간 : 40