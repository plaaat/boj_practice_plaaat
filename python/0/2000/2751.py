import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
a = [0] * 2000001 
for _ in range(N):
    b = int(input())
    a[b + 1000000] += 1  
for i in range(2000001):
    if a[i] > 0:
        print(f"{i - 1000000}\n" * a[i])#  ���� ��ȣ : 79658507, �޸� : 46744, �ð� : 1072