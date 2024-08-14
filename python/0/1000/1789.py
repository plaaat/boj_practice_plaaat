import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

a, b = 0, n

while a <= b:
    tem = (a + b) // 2
    num = tem * (tem + 1) // 2

    if num == n:
        print(tem)
        break
    elif num < n:
        a = tem + 1
    else:
        b = tem - 1
else:
    print(b)

# 제출 번호 : 82482962, 메모리 : 31120, 시간 : 44