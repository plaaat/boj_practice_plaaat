import sys

input = lambda: sys.stdin.readline().rstrip()

li = []
dic = {}
t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())
    num = (a ** 2 + b ** 2)
    if num in dic:
        dic[num].append(i)
    else:
        dic[num] = [i]
        li.append(num)

li.sort(reverse=True)

for i in li:
    for j in dic[i]:
        print(j)


# 제출 번호 : 82364009  메모리 : 31120  시간 : 32