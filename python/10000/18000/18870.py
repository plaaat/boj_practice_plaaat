import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
sli = sorted(set(li))
pli = {val:idx for idx,val in enumerate(sli)}
pr = []
for i in li:
  pr.append(pli[i])
print(*pr)


#  제출 번호 : 79646821, 메모리 : 144340, 시간 : 1940