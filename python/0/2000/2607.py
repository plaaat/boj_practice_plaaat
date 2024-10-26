import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
com = input()
li = list(input() for _ in range(t-1))

pn = 0
for w in li:
    tn = 0
    tl = list(com)
    tf = 1
    for i in w:
        try:tl.remove(i)
        except:
            if tf:
                tf = 0
                continue
            tf = -1
            break
    if tf != -1 and len(tl) < 2:
        pn += 1
print(pn)

# 제출 번호 : 85655375, 메모리 : 31120, 시간 : 32