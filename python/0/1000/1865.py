import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m,w = map(int,input().split())
    dis = [int(1e6)]*(n+1)
    dis[1] = 0
    li = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        li.append((a,b,c))
        li.append((b,a,c))
    for _ in range(w):
        a,b,c = map(int,input().split())
        li.append((a,b,-c))
    
    def bf():
        for i in range(n):
            for s,d,t in li:
                if dis[d] > dis[s]+t:
                    dis[d] = dis[s]+t
                    if i == n-1:
                        print('YES')
                        return
        print('NO')
        return
    bf()#  ���� ��ȣ : 81673035, �޸� : 31120, �ð� : 836