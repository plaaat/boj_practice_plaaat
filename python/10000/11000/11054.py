import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = list(map(int,input().split()))

dp1 = []
dp2 = []

li = [nli[0]]

for x in nli:
    if li[-1] < x:
        li.append(x)
        dp1.append(len(li))
    else:
        idx = bisect.bisect_left(li, x)
        li[idx] = x
        dp1.append(idx+1)

nli = nli[::-1]
li = [nli[0]]

for x in nli:
    if li[-1] < x:
        li.append(x)
        dp2.append(len(li))
    else:
        idx = bisect.bisect_left(li, x)
        li[idx] = x
        dp2.append(idx+1)
dp2 = dp2[::-1]

res = 0
for i in range(n):
    res = max(dp1[i]+dp2[i]-1, res)

print(res)

# 제출 번호 : 101914016, 메모리 : 34476, 시간 : 40