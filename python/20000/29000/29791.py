import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()

def cal(li,ct):
    tt = -1
    res = 0
    for i in li:
        if i >= tt:
            tt = i + ct
            res += 1
    return res

print(cal(a,100),cal(b,360))

# 제출 번호 : 95085749, 메모리 : 181264, 시간 : 1400