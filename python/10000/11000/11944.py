import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
m = min(n*len(str(n)),m)
n = str(n)
t = 0
while t != m:
    for i in n:
        if t == m:
            break
        print(i,end='')
        t += 1


#  제출 번호 : 84023052, 메모리 : 31120, 시간 : 32