import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))
find = 1
res = 0

for i in a:
    if i == find:
        find += 1
    else:
        res += 1

print(res)