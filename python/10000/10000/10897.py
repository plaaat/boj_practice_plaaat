import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tr = {}
for i in range(1,2 ** n + 1):
    tr[i] = 