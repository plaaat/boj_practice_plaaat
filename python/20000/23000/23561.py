import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list((map(int,input().split())))

li.sort()
num = []
for i in range(n):
    i += n
    num.append(li[i])

print(max(num) - min(num))

# 제출 번호 : 83720158, 메모리 : 66124,  시간 : 204