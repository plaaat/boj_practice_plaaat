import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
sli = sorted(set(li))
pli = {val:idx for idx,val in enumerate(sli)}
pr = []
for i in li:
  pr.append(pli[i])
print(*pr)#  ���� ��ȣ : 79646821, �޸� : 144340, �ð� : 1940