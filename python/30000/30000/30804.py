import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input().strip())
q = list(map(int, input().split()))

plen = 0
l = 0
li = {}

for r in range(n):
  if q[r] in li:
    li[q[r]] += 1
  else:
    li[q[r]] = 1
  while len(li) > 2:
    li[q[l]] -= 1
    if li[q[l]] == 0:
      del li[q[l]]
    l+=1
  plen = max(plen, r-l+1)

print(plen)
#  ���� ��ȣ : 79646504, �޸� : 34600, �ð� : 240