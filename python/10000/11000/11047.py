import sys
input = sys.stdin.readline

n,k = map(int,input().split())
li = [int(input()) for _ in range(n)]
a,b = 0,0
li.reverse()
for i in li:
  if a+i == k:
    b+=1
    break
  elif a+i < k:
    b+=((k-a)//i)
    a+=(i*((k-a)//i))
  else:
    continue
print(b)#  제출 번호 : 79650112, 메모리 : 31120, 시간 : 44