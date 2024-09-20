import sys
input = lambda: sys.stdin.readline().rstrip()

ty,tm,td = map(int,input().split())
n = int(input())
y31 = set([1,3,5,7,8,10,12])
for _ in range(n):
    a,b,c = map(int,input().split())
    tf = 2
    for y,m,d in [[a,b,c],[c,b,a],[c,a,b]]:
        if 0 < m < 13:
            if m == 2:
                if d > (29 if y % 4 == 0 else 28) or d == 0:
                    continue
                elif (ty,tm,td) > (y,m,d):
                    tf = 1
                    break
                else:
                    tf = 0
            elif m in y31:
                if d > 31 or d == 0:
                    continue
                elif (ty,tm,td) > (y,m,d):
                    tf = 1
                    break
                tf = 0
            else:
                if d > 30 or d == 0:
                    continue
                elif (ty,tm,td) > (y,m,d):
                    tf = 1
                    break
                tf = 0
    if tf == 1:
        print('unsafe')
    elif tf == 0:
        print('safe')
    else:
        print('invalid')
        
# 제출 번호 : 84102900,  메모리 : 31120,  시간 : 736
# 이왜실4.. 구현개커차나.