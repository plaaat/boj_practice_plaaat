import sys
input = lambda: sys.stdin.readline().rstrip('\n')

y = input()
y,m,d = y[0:4],y[4:6],y[6:]
t = int(input())
mn = -1
pn = []
cal = lambda x,y: sum((int(x[i]) - int(y[i])) ** 2 for i in range(len(x)))

for _ in range(t):
    tn = 1
    ty = input()
    tty,tm,td = ty[0:4],ty[4:6],ty[6:]
    tn *= cal(y,tty)
    tn *= cal(m,tm)
    tn *= cal(d,td)
    if tn > mn:
        mn = tn
        pn = [ty]
    elif tn == mn:
        pn.append(ty)

print(sorted(pn)[0])

# 제출 번호 : 85308275, 메모리 : 31120, 시간 : 44
# 아아아아아악. 메첸. 왜틀리나햇ㄴ