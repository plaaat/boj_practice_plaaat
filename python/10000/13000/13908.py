import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
nli = list(map(int, input().split()))
pn = 0


def dfs(li, tn):
    global pn
    if tn == n:
        li = set(li)
        for i in nli:
            if not i in li:
                break
        else:
            pn += 1
        return

    for i in range(10):
        li.append(i)
        dfs(li, tn + 1)
        li.pop()


for i in range(10):
    dfs([i], 1)

print(pn)



#  제출 번호 : 83040941, 메모리 : 31120, 시간 : 4124