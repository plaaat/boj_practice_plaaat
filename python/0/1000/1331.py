import sys
input = lambda: sys.stdin.readline().rstrip()

x = input()
visit = set()
a,b = ord(x[0]) - 65,int(x[1])
sa = a
sb = b

visit.add(x)
for _ in range(35):
    x = input()
    visit.add(x)
    aa,bb = ord(x[0]) - 65,int(x[1])
    if (abs(aa - a) == 2 and abs(bb - b) == 1) or (abs(aa - a) == 1 and abs(bb - b) == 2):
        a = aa
        b = bb
    else:
        print('Invalid')
        break
else:
    if len(visit) == 36 and ((abs(sa - a) == 2 and abs(sb - b) == 1) or (abs(sa - a) == 1 and abs(sb - b) == 2)):
        print('Valid')
    else:
        print('Invalid')

# 제출 번호 : 91226977, 메모리: 32412, 시간 : 32 