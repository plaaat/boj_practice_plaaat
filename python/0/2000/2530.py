t,m,s = map(int,input().split())
n = int(input())
nt = 0
nm,ns = divmod(n,60)
if nm != 0:nt,nm = divmod(nm,60)
if s+ns>=60:
    nm+=1
    s = s+ns-60
    ns = 0
if m+nm >= 60:
    nt+=1
    m = m+nm-60
    nm = 0
if t+nt>=24:
    t = (t+nt)%24
    nt = 0
print(t+nt,m+nm,s+ns)#  제출 번호 : 80809627, 메모리 : 31120, 시간 : 40