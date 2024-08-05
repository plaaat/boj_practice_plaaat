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
print(*c)#  제출 번호 : 79654405, 메모리 : 120696, 시간 : 136