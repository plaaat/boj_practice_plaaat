import sys
input = lambda: sys.stdin.readline().rstrip()

wo = input()
n = input()
li = input().split()
pli = []
sn = 0

for i in li:
    if i == 'int':
        pli.append(int(wo[sn:sn+8],16))
        sn+=8
    elif i == 'char':
        pli.append(int(wo[sn:sn+2],16))
        sn+=2
    else:
        pli.append(int(wo[sn:sn+16],16))
        sn+=16

print(*pli)

# 제출 번호 : 83212555,  메모리 : 46660,  시간 : 156