import sys
input = sys.stdin.readline
a = int(input())
b = set(input().split())
c = int(input())
d = input().split()
for i in range(c):
  if d[i] in b:
    print(1)
  else:
    print(0)



#  제출 번호 : 79654362, 메모리 : 139752, 시간 : 188