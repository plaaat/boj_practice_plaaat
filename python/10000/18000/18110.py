import sys
input = sys.stdin.readline
def round(x):
  x = str(x).split(".")
  if int(x[1][0]) >= 5:
    return int(x[0])+1
  else:
    return int(x[0])
a = int(input())
if a == 0:
  print("0")
else:  
  b = []
  for _ in range(a):
    b.append(int(input()))
  pa = round(a*(15/100))
  b.sort()
  if pa == 0:
    print(round(sum(b)/len(b)))
  else:
    del b[:pa]
    del b[-pa:]
    print(round(sum(b)/len(b)))#  ���� ��ȣ : 79653951, �޸� : 35360, �ð� : 176