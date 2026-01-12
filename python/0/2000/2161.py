import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
nli = deque(range(2,n+1))
rli = [1]

while nli:
    nli.append(nli.popleft())
    rli.append(nli.popleft())

print(*rli)

# 제출 번호 : 101823768, 메모리 : 34900, 시간 : 64