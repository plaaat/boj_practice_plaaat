import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, m = map(int, input().split())
  li = list(map(int, input().split()))
  cnt = 0
  while True:
      maxl= max(li)
      if li[0] == maxl and m == 0:
        print(cnt+1)
        break
      elif li[0] == maxl:
        li.pop(0) 
        cnt += 1
        m -= 1
      else:
        li.append(li.pop(0))
        if m == 0:
          m = len(li) - 1
        else:
          m -= 1


#  제출 번호 : 79653841, 메모리 : 31120, 시간 : 40