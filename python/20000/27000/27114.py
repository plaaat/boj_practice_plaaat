import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(a, b, c, k):
    queue = deque([(0, 0, 0)])
    vis = set()

    while queue:
        en, an, n = queue.popleft()

        if en == k and an & 3 == 0:
            return n
        an = an & 3
        if en > k or (en, an) in vis:
            continue

        vis.add((en, an))

        for ten, tan in [(en + a, an - 1), (en + b, an + 1), (en + c, an + 2)]:
            if ten <= k and (ten, tan) not in vis:
                queue.append((ten, tan, n + 1))

    return -1

a, b, c, k = map(int, input().split())
print(bfs(a, b, c, k))

# 제출 번호 : 84264032,  메모리 : 466256,  시간 : 4652   by.pypy3
# 에라야팔안풀어.