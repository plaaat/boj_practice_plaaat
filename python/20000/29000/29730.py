import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
boj = []
wol = []
for _ in range(t):
    wo = input()
    if wo[0:7] == 'boj.kr/':
        wo = wo.lstrip("boj.kr/")
        try:
            boj.append(int(wo))
        except:
            wol.append(f'boj.kr/{wo}')
    else:
        wol.append(wo)

wol.sort()
wol.sort(key = lambda x: len(x))

if wol:print(*wol,sep='\n')
boj.sort()
for x in boj:print(f"boj.kr/{x}")

# 제출 번호 : 95356101, 메모리 : 32412, 시간 : 36