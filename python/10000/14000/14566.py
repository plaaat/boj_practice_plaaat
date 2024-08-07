import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

li = list(map(int,input().split()))

m = float('inf')

li.sort()

num = 0

for i in range(1,n):

  tem = li[i]-li[i-1]

  if tem<m:

    m = tem

    num = 1

  elif tem == m:

    num+=1

print(m,num)


#  제출 번호 : 79641425, 메모리 : 31120, 시간 : 36