import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())
st = set(range(1,n+1))
mst = max(st)

a = list(map(int,input().split()))
for i in a:
    while i <= mst:
        if i in st:
            st.remove(i)
            break
        else:
            i += k

print(0 if st else 1)

# 제출 번호 : 90190639, 메모리 : 32412, 시간 : 36