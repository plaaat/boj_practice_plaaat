import sys
input = lambda: sys.stdin.readline().rstrip()
def rec(lvl, seq):
    if not seq:
        return
    mid = len(seq) // 2
    tr[lvl].append(seq[mid])
    rec(lvl + 1, seq[:mid])
    rec(lvl + 1, seq[mid + 1:])
k = int(input())
tr = [[] for _ in range(k)]
lst = list(map(int, input().split()))
rec(0,lst)
for i in tr:
    print(*i)



#  제출 번호 : 83997698, 메모리 : 31120, 시간 : 32