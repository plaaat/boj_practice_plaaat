import sys
input = lambda:sys.stdin.readline()
sys.setrecursionlimit(10**6)

nli = []
while True:
    try:
        n = int(input())
        nli.append(n)
    except:break

def fin(li):
    lli = len(li)
    if lli == 0:
        return
    left = []
    right = []
    mid = li[0]
    tf = True
    for i in range(1,lli):
        if li[i] > mid:
            left = li[1:i]
            right = li[i:]
            tf = False
            break
    if tf:
        left = li[1:]
    fin(left)
    fin(right)
    print(mid)

fin(nli)#  제출 번호 : 80328889, 메모리 : 424776, 시간 : 2464