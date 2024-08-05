import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = []
for _ in range(n):
  a,b = map(int,input().split())
  li.append((b,a))
li.sort()
num = 0
re = 0
for i in li:
  if i[1]<re:
    continue
  else:
    num+=1
    re = i[0]
print(num)#  제출 번호 : 79646796, 메모리 : 44580, 시간 : 228