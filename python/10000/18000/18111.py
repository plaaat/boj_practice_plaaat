import sys
input=lambda:sys.stdin.readline().rstrip()

n,m,b = map(int,input().split())
li = []
pli = [0]*257
for i in range(n):
  li.extend(map(int,input().split()))
p = 0
for i in range(257):
  cb = b
  for s in li:
    if s<=i:
      pli[i] += i-s
      cb-=i-s
    else:
      pli[i]+=2*(s-i)
      cb+=s-i
  if cb>=0 and pli[i]<=pli[p]:
    p = i
print(pli[p], p)


#  제출 번호 : 79649886, 메모리 : 121776, 시간 : 548