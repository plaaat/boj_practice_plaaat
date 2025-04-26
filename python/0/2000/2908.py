import sys
input = lambda: sys.stdin.readline().rstrip()

a,b = input().split()
rv = lambda x: int(x[2]+x[1]+x[0])
print(max(rv(a),rv(b)))

# 제출번호 : 92496226, 메모리 : 32412, 시간 : 36