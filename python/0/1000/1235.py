import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
li = [input() for _ in range(t)]
s = set()
p = len(li[0])
pn = 0
while True:
    pn += 1
    if pn == p:
        break
    for i in li:
        tem = i[-pn:]
        if tem in s:
            break
        else:
            s.add(tem)
    if len(s) == t:
      break
    else:
      s = set()
print(pn)


#  제출 번호 : 83856214, 메모리 : 31120, 시간 : 44