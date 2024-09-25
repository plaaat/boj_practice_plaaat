import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
d31 = set([1,3,5,7,8,10,12])
for _ in range(t):
    a,b = map(int,input().split())
    y,m,d = a,b,b
    if d - b <= 0:
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
        if m == 2:
            print(y,m,d-b+(29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28))
        else:print(y,m,d-b+(31 if m in d31 else 30))
    else:
        print(y,m,d-b)
        
# 제출 번호 : 84312589, 메모리 : 31120, 시간 : 32
