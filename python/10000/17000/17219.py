import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pw = {}
for _ in range(n):
  s,p = input().strip().split()
  pw[s] = p
for _ in range(m):
  print(pw.get(input().strip()))#  제출 번호 : 79650079, 메모리 : 49208, 시간 : 232