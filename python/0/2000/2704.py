import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    fb = lambda x: format(x,'b')
    cz = lambda x: '0' * (6 - len(x)) + x
    bh,bm,bs = map(cz,map(fb,map(int,input().split(':'))))
    a1 = bh + bm + bs
    a2 = ''
    for i in range(6):
        a2 += bh[i] + bm[i] + bs[i]
    print(a2, a1)

# 제출 번호 : 98334673, 메모리 : 32412, 시간 : 36