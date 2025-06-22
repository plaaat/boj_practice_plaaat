import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
nli = [0 for _ in range(n)]
mli = [0 for _ in range(m)]
mn = -1
mn_loc = 0
mn_fl = True

for i in range(n):
    inp1 = list(input().split())
    for j in range(m):
        num = inp1[j].count('9')
        mli[j] += num
        if mn < mli[j]:
            mn = mli[j]
            mn_loc = j
            mn_fl = True
        nli[i] += num
        if mn < nli[i]:
            mn = nli[i]
            mn_loc = i
            mn_fl = False

if not mn_fl:
    print(sum(nli) - nli[mn_loc])
else:
    print(sum(mli) - mli[mn_loc])

# 제출 번호 : 95566412, 메모리 : 32412, 시간 : 112