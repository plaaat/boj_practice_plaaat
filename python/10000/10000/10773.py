import sys
from collections import deque
input = sys.stdin.readline
a = deque()
for i in range(int(input())):
  b = int(input())
  if b != 0:
    a.appendleft(b)
  else:
    a.popleft()
print(sum(a))



#  제출 번호 : 79654087, 메모리 : 34008, 시간 : 100