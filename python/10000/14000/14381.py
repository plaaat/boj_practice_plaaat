import sys

input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n == 0:
        print(f'Case #{i}: INSOMNIA')
    else:
        vis = set()
        num = 0
        pn = 0
        tf = True
        while tf:
            num += 1
            tn = str(num * n)
            for s in str(tn):
                if not s in vis:
                    if pn == 9:
                        print(f'Case #{i}: {tn}')
                        tf = False
                        break
                    else:
                        pn += 1
                        vis.add(s)


# 제출 번호 : 82612055  메모리 : 31120  시간 : 28
