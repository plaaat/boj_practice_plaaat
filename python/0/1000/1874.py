import sys
input = sys.stdin.readline

n = int(input())
li = []#수 입력
for i in range(n):
  li.append(int(input()))
st = []#스택
pli = []#프린트 기록
tf = True
a = 1

for i in li:
    if not tf:
      break
    while a <= i:
        st.append(a)
        pli.append('+')
        a += 1

    while st[-1] >= i:
        if st[-1] == i:
            del st[-1]
            pli.append('-')
            break
        else:
            print('NO')
            tf = False
            break
if tf:
  print(*pli, sep = '\n')


#  제출 번호 : 79653817, 메모리 : 41252, 시간 : 168