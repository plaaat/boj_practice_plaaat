import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()

st = set(range(97,123))
wo = input()


if len(wo) != 26:
    print(wo + chr(min(st-set([ord(i) for i in wo]))))
else:
    i = 24
    while wo[i] >= wo[i+1] and i > -1:
        i-=1
    if i == -1:
        print(-1)
    else:
        tn = 25
        while wo[tn] <= wo[i]:
            tn -= 1
        pwo = list(wo)
        pwo[i],pwo[tn] = pwo[tn],pwo[i]
        print(*pwo[:i + 1],sep='')

# 제출 번호 : 85436530, 메모리 : 33184, 시간 : 36