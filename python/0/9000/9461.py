import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):

  li = [1,1,1,2,2]

  n = int(input())

  if n<=5:

    print(li[n-1])

  else:

    while len(li) != n:

      li.append(li[-1]+li[-5])

    print(li[-1])#  ���� ��ȣ : 79649851, �޸� : 31120, �ð� : 40