import sys
input = lambda:sys.stdin.readline().rstrip()
li = ['January','February','March','May','April','June','July']
while True:
  n,w = input().split()
  n = int(n)
  if n == 0 and w == '#':
    break
  if w == 'August' and n == 4:
    print('Happy birthday')
  elif w == 'February' and n == 29:
    print('Unlucky')
  elif w in li:
    print('Yes')
  elif w == 'August' and n < 4:
    print('Yes')
  else:
    print('No')
  #  ���� ��ȣ : 79646448, �޸� : 31120, �ð� : 40