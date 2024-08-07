import sys
input = sys.stdin.readline

n,m = map(int,input().split())
p = {}
for i in range(n):
  na = input().strip()
  p[str(i+1)] = na
  p[na] = str(i+1)

for _ in range(m):
  print(p.get(input().strip()))


#  제출 번호 : 79650137, 메모리 : 60816, 시간 : 276