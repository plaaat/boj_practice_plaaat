import sys
input = lambda:sys.stdin.readline().rstrip()
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L[m][n]

X = input()
Y = input()
print(lcs(X,Y))#  제출 번호 : 80264228, 메모리 : 55708, 시간 : 316