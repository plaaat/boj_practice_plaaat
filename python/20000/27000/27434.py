import sys
import functools

input = sys.stdin.readline

n = int(input().strip())

print(functools.reduce(lambda x, y: x * y, range(1, n + 1), 1))



#  제출 번호 : 89309976, 메모리 : 212544, 시간 : 3068