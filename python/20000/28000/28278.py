import sys

input = sys.stdin.readline

t = int(input())
q = []
ql = 0

for _ in range(t):
    n = input().rstrip()
    if len(n) == 1:
        n = int(n)
        if n == 2:
            if ql == 0:
                print(-1)
            else:
                print(q.pop())
                ql-=1
        elif n == 3:
            print(ql)
        elif n == 4:
            print(1 if ql == 0 else 0)
        else:
            print(q[-1] if ql != 0 else -1)
    else:
        n,a = map(int,n.split())
        q.append(a)
        ql+=1#  제출 번호 : 82080853, 메모리 : 71112, 시간 : 992