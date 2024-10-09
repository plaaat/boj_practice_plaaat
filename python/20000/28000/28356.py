import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = [[0 for _ in range(m)] for _ in range(n)]
d = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
pn = 1
st = set([1])

for i in range(n):
    for j in range(m):
        tst = st.copy()
        for dx,dy in d:
            dx += j
            dy += i
            if 0 <= dx < m and 0 <= dy < n and li[dy][dx] in tst:
                tst.remove(li[dy][dx])
        if not tst:
            pn += 1
            li[i][j] = pn
            st.add(pn)
        else:
            li[i][j] = tst.pop()

print(pn)
for i in li:print(*i)

# 제출번호 : 84792599, 메모리 : 123044, 시간 : 380, By.pypy3