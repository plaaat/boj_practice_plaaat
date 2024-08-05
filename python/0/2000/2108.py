import sys
input = sys.stdin.readline

a = []
b = [0] * 8001
c = int(input())
e=0
for i in range(c):
  d =int(input())
  e+=d
  a.append(d)
  b[d+4000] += 1
a.sort()
bl = max(b)
asu = e/c
if asu >=0 and asu-int(asu) >= 0.5:
  print(int(asu)+1)
elif asu<0 and int(asu)-asu >= 0.5:
  print(int(asu)-1)
else:
  print(int(asu))
print(a[c//2])
if b.count(bl) == 1:
  print(b.index(max(b))-4000)
else:
  del b[b.index(bl)]
  bl = max(b)
  print(b.index(max(b))-3999)
print(a[-1]-a[0])#  제출 번호 : 79653985, 메모리 : 52504, 시간 : 432