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
#  ���� ��ȣ : 79654087, �޸� : 34008, �ð� : 100