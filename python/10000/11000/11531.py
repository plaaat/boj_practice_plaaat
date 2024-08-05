import sys
input = lambda:sys.stdin.readline().rstrip()

dic = {}
sol = 0
pen = 0

while True:
    try:
        t,p,a = input().split()
        if a == 'right':
            sol+=1
            if p in dic:
                pen+=(dic[p]*20+int(t))
            else:pen+=int(t)
        else:
            if p in dic:
                dic[p]+=1
            else:
                dic[p] = 1
    except:
        print(sol,pen)
        break#  제출 번호 : 81518787, 메모리 : 31120, 시간 : 40