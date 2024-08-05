import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = [input().rstrip() for _ in range(N)]

minb = 65

for r in range(N - 7):
    for c in range(M - 7):
        w = 0
        b = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if B[r + i][c + j] == 'B':
                        w += 1
                    else:
                        b += 1
                else:
                    if B[r + i][c + j] == 'W':
                        w += 1
                    else:
                        b += 1
        minb = min(minb, w, b)

print(minb)#  ���� ��ȣ : 79654262, �޸� : 31120, �ð� : 84