import sys
import math
input = sys.stdin.readline
a = math.factorial(int(input()))
a = str(a)
b = 0
c = 0
while True:
  c-=1
  if a[c] == "0":
    b+=1
  else:
    break
print(b)#  ���� ��ȣ : 79654007, �޸� : 33240, �ð� : 44