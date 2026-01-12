import sys
input = lambda: sys.stdin.readline().rstrip()
import bisect

n = int(input())
nli = tuple(map(int, input().split()))
li = [nli[0]]
rec = [0] * n
rec[0] = 1

for i in range(1, n):
    if li[-1] >= nli[i]:
        idx = bisect.bisect_left(li,nli[i])
        li[idx] = nli[i]
        rec[i] = idx + 1
    else:
        li.append(nli[i])
        rec[i] = len(li)

tarlen = len(li)
res = []
for i in range(n):
    i = n - i - 1
    if rec[i] == tarlen:
        res.append(nli[i])
        tarlen -= 1
    
    if tarlen == 0:
        break

print(len(li))
print(*res[::-1])

# 제출 번호 : 101858988, 메모리 : 153256, 시간 : 1336