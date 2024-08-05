import sys
input = sys.stdin.readline

a=0
n,m = map(int,input().split())
k = set()
uk = []
for _ in range(n):
  k.add(input().strip())
for _ in range(m):
  wo = input().strip()
  if wo in k:
    uk.append(wo)
    a+=1
print(a)
uk.sort()
print(*uk, sep='\n')#  제출 번호 : 79653754, 메모리 : 37264, 시간 : 76