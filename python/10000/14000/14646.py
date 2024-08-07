import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
vis = set()
num = list(map(int,input().split()))
pn = 0
mn = 0
for i in num:
    if not i in vis:
        vis.add(i)
        pn+=1
    elif i in vis:
        pn-=1
    mn = max(mn,pn)
print(mn)


#  제출 번호 : 81176960, 메모리 : 54036, 시간 : 176