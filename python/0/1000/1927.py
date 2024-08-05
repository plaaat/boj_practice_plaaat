import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

li = []
lim = []
a = 0
b = 0
m = int(input())
for _ in range(m):
    n = int(input())
    if n == 0:
        if a == 0 and b == 0:
            print(0)
        else:
            if a == 0:
              print(-heapq.heappop(lim))
              b-=1
            elif b == 0:
              print(heapq.heappop(li))
              a-=1
            elif li[0] >= lim[0]:
              print(-heapq.heappop(lim))
              b-=1
            else:
              print(heapq.heappop(li))
              a-=1
    elif n<0:
      heapq.heappush(lim, -n)
      b+=1
    else:
      heapq.heappush(li, n)
      a+=1#  제출 번호 : 79649803, 메모리 : 37044, 시간 : 136