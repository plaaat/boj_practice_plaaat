import sys
input = lambda: sys.stdin.readline().rstrip()

st = {}
t = int(input())
for _ in range(t):
    wo = input().split()
    for i in range(2, len(wo)):
        if wo[i] in st:
            st[wo[i]] += 1
        else:
            st[wo[i]] = 1
sti = list(st.items())
sti.sort(key = lambda x:x[1])
if len(sti) == 1:
    print(sti[0][0])
else:
    if sti[-1][1] == sti[-2][1]:
        print(-1)
    else:
        print(sti[-1][0])

# 제출 번호 : 94334379, 메모리 : 52064, 시간 : 108
