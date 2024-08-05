import sys
input = sys.stdin.readline

n = int(input())
li = []#ìˆ˜ ì…ë ¥
for i in range(n):
  li.append(int(input()))
st = []#ìŠ¤íƒ
pli = []#í”„ë¦°íŠ¸ ê¸°ë¡
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
  print(*pli, sep = '\n')#  Á¦Ãâ ¹øÈ£ : 79653817, ¸Ş¸ğ¸® : 41252, ½Ã°£ : 168