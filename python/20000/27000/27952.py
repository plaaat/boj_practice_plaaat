def main():
    import sys
    input = sys.stdin.readline
    N,X = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_b = 0
    for i in range(N):
      sum_b+=b[i]
      if sum_b < a[i]:
        print(-1)
        return
    print((sum_b - a[-1])//X)
if __name__ == "__main__":
    main()


#  제출 번호 : 79646182, 메모리 : 109752, 시간 : 352