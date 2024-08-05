import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l1 = []
l2 = []
ls = set()
for _ in range(m):
  ma,mb = map(int,input().split())
  a,b = min(ma,mb), max(ma,mb)
  l1.append(a)
  l2.append(b)
tf = 0
p = 0

while p!=n:
  for i in range(len(l1)):
    if l1[0] == 1 or l1[0] in ls:
      ls.add(l2.pop(0))
      del l1[0]
    elif l2[0]==1 or l2[0] in ls:
      ls.add(l1.pop(0))
      del l2[0]
    else:
      l2.append(l2.pop(0))
      l1.append(l1.pop(0))
  p+=1
print(len(ls))#  제출 번호 : 79650050, 메모리 : 31120, 시간 : 40