import sys
input = sys.stdin.readline
N = int(input())
li = []

for _ in range(N):
    w, h = map(int, input().split())
    li.append((w, h))

rank = [1] * N

for i in range(N):
    for j in range(N):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            rank[i] += 1

print(*rank)#  제출 번호 : 79654243, 메모리 : 31120, 시간 : 40