import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
st = {li[i]:i for i in range(n)}
eli = list(map(int,input().split()))

for i in range(n):
    st[eli[i]] -= i

st = list(st.items())
st.sort(key=lambda x: -x[1])

reli = []
reli.append(st[0][0])
la = st[0][1]
for i in range(1,n):
    if la != st[i][1]:
        break
    reli.append(st[i][0])

print(*reli)

# 제출 번호 : 94599330, 메모리 : 57416, 시간 : 192