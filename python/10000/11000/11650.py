import sys

input = sys.stdin.readline

x = []

m = int(input())

for _ in range(m):

  a,b = map(int,input().split())

  x.append([a,b])

x.sort()

for i in range(m):

  print(*x[i])#  제출 번호 : 79658430, 메모리 : 122664, 시간 : 372