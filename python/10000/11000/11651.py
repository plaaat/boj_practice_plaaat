import sys
input = sys.stdin.readline
li = []
for _ in range(int(input())):
  a,b = map(int,input().split())
  li.append((b,a))
li.sort()
for i in range(len(li)):
  print(li[i][1],li[i][0])#  ���� ��ȣ : 79654075, �޸� : 44580, �ð� : 320