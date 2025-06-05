import sys
from decimal import Decimal,getcontext
input = lambda: sys.stdin.readline().rstrip()

getcontext().prec = 20
def uclid(ax,ay,bx,by):
    return ((ax - bx) ** 2 + (ay - by) ** 2).sqrt()

ax,ay,bx,by,px,py,r = map(Decimal,input().split())

dd = uclid(ax,ay,bx,by)
pd = max(0,uclid(ax,ay,px,py) - r) + max(0,uclid(bx,by,px,py) - r)
print(f"{min(dd,pd):0.15f}")

# 제출 번호 : 95086605, 메모리 : 38408, 시간 : 64