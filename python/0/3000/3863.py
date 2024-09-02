import sys
input = lambda: sys.stdin.readline().rstrip()
while True:
    n,m = map(int,input().split())
    if n==0 and m == 0:
        break
    dl = []
    for _ in range(n):
        a,b,c,d = map(int,input().split())
        dl.append([c,d])
    for _ in range(m):
        x,y = map(int,input().split())
        tn = 0
        if y == 0:
            print(0)
            continue

        for a,b in dl:
            if x <= a < x+y or x < a+b <= x+y or a <= x and a+b > x:
                tn+=1
        print(tn)


# 제출 번호 : 83262528, 메모리 : 32140, 시간 : 1544