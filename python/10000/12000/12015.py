import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect

n = int(input())
nli = tuple(map(int, input().split()))
li = [nli[0]]

for i in range(1, n):
    if li[-1] > nli[i]:
        li[bisect.bisect_left(li,nli[i])] = nli[i]
    else:
        li.append(nli[i])

print(len(li))

# 제출 번호 : 101858397, 메모리 : 138856, 시간 : 836