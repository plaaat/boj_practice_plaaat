import sys

input = lambda: sys.stdin.readline().rstrip()

dp = {}
n = int(input())


def fib(n):
    if n <= 2 or n in dp:
        return dp[n]

    tn = n // 2
    if n % 2 == 0:
        n1 = fib(tn)
        n2 = fib(tn - 1)
        dp[n] = ((2 * n2 + n1) * n1) % 1000000007
    else:
        n1 = fib(tn + 1)
        n2 = fib(tn)
        dp[n] = (n1**2 + n2**2) % 1000000007
    return dp[n]


dp[0], dp[1], dp[2] = 0, 1, 1
pn = fib(n)
print(pn)


# 제출 번호 : 82745081,  메모리 : 31120,  시간 : 36
