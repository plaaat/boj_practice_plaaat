import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

li = []
a = 0
m = int(input())
for _ in range(m):
    n = int(input())
    n = -n
    if n == 0:
        if a == 0:
            print(0)
        else:
            a-=1
            print(-heapq.heappop(li))
    else:
        heapq.heappush(li, n)
        a+=1
#  ���� ��ȣ : 79649827, �޸� : 37044, �ð� : 136