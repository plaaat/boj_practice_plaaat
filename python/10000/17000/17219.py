import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pw = {}
for _ in range(n):
  s,p = input().strip().split()
  pw[s] = p
for _ in range(m):
  print(pw.get(input().strip()))#  ���� ��ȣ : 79650079, �޸� : 49208, �ð� : 232