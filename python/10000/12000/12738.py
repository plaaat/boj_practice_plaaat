import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect

n = int(input())
nli = tuple(map(int, input().split()))
li = [nli[0]]

for i in range(1, n):
    if li[-1] >= nli[i]:
        li[bisect.bisect_left(li,nli[i])] = nli[i]
    else:
        li.append(nli[i])

print(len(li))

# 제출 번호 : 101858549, 메모리 : 153240, 시간 : 808