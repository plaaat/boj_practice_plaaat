import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = tuple(map(int,input().split()))
mil,mal = 0,1000000000
mid = 0
pn = 0
rec = (0,0,0,0)
while mil!=mid or mal!=mid:
  num = 0
  mid = (mil+mal)//2
  for i in li:
    if i>mid:
      num+=(i-mid)
  if pn<mid:
    pn = mid
  if num >= m:
    mil = mid
  else:
    mal = mid
  if (pn,mid,mil,mal) == rec:
    break
  rec = (pn,mid,mil,mal)
print(mid)#  ���� ��ȣ : 79660055, �޸� : 267648, �ð� : 548