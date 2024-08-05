import sys
input = sys.stdin.readline
a = []
def deque():
  b = input().split()
  if b.count("push_front") == 1:
    if len(a) == 0:
      a.append(b[1])
    else:
      a.insert(0,b[1])
  elif b.count('push_back') == 1:
    a.append(b[1])
  elif b.count('pop_front') == 1:
    if len(a) == 0:
      print("-1")
    else:
      print(a.pop(0))
  elif b.count('pop_back') == 1:
    if len(a) == 0:
      print("-1")
    else:
      print(a.pop())
  elif b.count('size') == 1:
    print(len(a))
  elif b.count('empty') == 1:
    if len(a) == 0:
      print("1")
    else:
      print("0")
  elif b.count('front') == 1:
    if len(a) == 0:
      print("-1")
    else:
      print(a[0])
  elif b.count('back') == 1:
    if len(a) == 0:
      print("-1")
    else:
      print(a[len(a)-1])
 
for _ in range (int(input())):
  deque()#  제출 번호 : 79658445, 메모리 : 113076, 시간 : 176