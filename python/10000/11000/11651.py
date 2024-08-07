import sys
input = sys.stdin.readline
li = []
for _ in range(int(input())):
  a,b = map(int,input().split())
  li.append((b,a))
li.sort()
for i in range(len(li)):
  print(li[i][1],li[i][0])


#  제출 번호 : 79654075, 메모리 : 44580, 시간 : 320