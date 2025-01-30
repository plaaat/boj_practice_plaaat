import sys
from decimal import Decimal,getcontext
import re
input = lambda: sys.stdin.readline().rstrip()

getcontext().prec = 100

t = int(input())
for i in range(t):
    li = []
    while True:
        n = input()
        if n == '0':
            print(re.sub(r"\.?0+$", "", str(sum(li))))
            break
        li.append(Decimal(n))



#  제출 번호 : 85191610, 메모리 : 37332, 시간 : 92