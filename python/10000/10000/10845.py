from collections import deque
import sys
input = sys.stdin.readline
a = deque()
for _ in range(int(input())):
  b = deque(input().split())
  if len(b) == 2:
    a.append(b[1])
  elif b[0] == "pop":
    if len(a) == 0:
      print("-1")
    else:
      print(a.popleft())
  elif b[0] == "size":
    print(len(a))
  elif b[0] == "empty":
    if len(a) == 0:
      print(1)
    else:
      print(0)
  elif b[0] == "front":
    if len(a) == 0:
      print("-1")
    else:
      print(a[0])
  elif b[0] == "back":
    if len(a) == 0:
      print("-1")
    else:
      print(a[-1])


#  제출 번호 : 79654376, 메모리 : 115472, 시간 : 204