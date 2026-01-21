import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

n, k = map(int,input().split())
crys = []

for _ in range(n):
    m,v = map(int,input().split())
    crys.append((m,v))
crys.sort()

bags = [int(input()) for _ in range(k)]
bags.sort()
res = 0

tq = []
cryind = 0

for b in bags:
    while cryind < n and crys[cryind][0] <= b:
        heapq.heappush(tq, -crys[cryind][1])
        cryind += 1
    if tq:
        res -= heapq.heappop(tq)

print(res)

# 제출 번호 : 102103413, 메모리 : 99460, 시간 : 1292