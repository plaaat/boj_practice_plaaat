import sys
import re

input = lambda: sys.stdin.readline().rstrip()

t = int(input())
check = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(t):
    wo = input()
    if check.match(wo):
        print('Infected!')
    else:
        print('Good')

# 제출 번호 : 83011304,  메모리 : 34752,  시간 : 92