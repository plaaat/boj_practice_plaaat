import sys
input = sys.stdin.readline

n = int(input())
wo = input().strip()
vis = set([(0,0)])
dic={'E':(1,0),'W':(-1,0),'N':(0,1),'S':(0,-1)}
now = (0,0)
num = 1
for i in wo:
    x,y = dic[i]
    now = (now[0]+x,now[1]+y)
    if not now in vis:
        vis.add(now)
        num+=1
print(num)#  제출 번호 : 81539311, 메모리 : 31120, 시간 : 40