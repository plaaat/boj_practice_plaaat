from collections import deque
import sys

input = sys.stdin.readline
a = int(input())

c = deque(range(1, a + 1))
start = 1
end = a

while len(c) != 1:
  c.popleft()
  c.append(c.popleft())
print(*c)#  ���� ��ȣ : 79654405, �޸� : 120696, �ð� : 136