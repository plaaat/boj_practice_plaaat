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
print(*uk, sep='\n')#  ���� ��ȣ : 79653754, �޸� : 37264, �ð� : 76