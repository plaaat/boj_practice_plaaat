import sys
input = sys.stdin.readline
b = []
for i in range(int(input())):
  a =  list(input().split())
  if a[0] == "push":
    b.append(a[1])
  elif a[0] == "pop":
    if len(b) ==0:
      print("-1")
    else:
      print(b.pop(-1))
  elif a[0] == "empty":
    if len(b) ==0:
      print(1)
    else:
      print(0)
  elif a[0] == "size":
    print(len(b))
  elif a[0] == "top":
    if len(b) ==0:
      print("-1")
    else:
      print(b[-1])#  ���� ��ȣ : 79654471, �޸� : 112008, �ð� : 172