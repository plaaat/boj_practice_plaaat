import sys

input = lambda: sys.stdin.readline().rstrip()

wo = input()
pli = []
tn = 0
li = []

for i in wo:
    if i == "X":
        tn+=1
    else:
        pli.append(tn)
        tn = 0
        pli.append(".")
pli.append(tn)

for i in pli:
    if i == '.':
        li.append('.')
    else:
        if i % 4 == 0:
            for _ in range(i//4):
                li.append('AAAA')
        elif i % 4 == 2:
            if i > 4:
                for _ in range(i//4):
                    li.append('AAAA')
                li.append('BB')
            else:
                li.append('BB')
        else:
            print(-1)
            exit(0)

print(''.join(li))


# 제출 번호 : 82506175,  메모리 : 31120, 시간 : 40
