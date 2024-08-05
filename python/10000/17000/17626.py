import sys
input = sys.stdin.readline

n = int(input())
rn = n**(0.5)
pl = 4

if rn == int(rn):
  print(1)
else:
  tf = True
  rn = int(rn)+1
  while tf:
    cn = n
    rn-=1
    if rn == 0:
      if pl == 3:
        print(3)
      else:
        print(4)
      break
    cn -= rn**2
    rrn = cn**0.5
    if rrn == int(rrn):
      print(2)
      tf = False
    else:
      rrn = int(rrn)+1
      ttf = True
      while ttf:
        ccn = cn
        rrn-=1
        ccn -= rrn**2
        rrrn = ccn**0.5
        if ccn<0:
          break
        elif rrrn == int(rrrn):
          ttf = False
          pl = 3
          break#  제출 번호 : 79650030, 메모리 : 31120, 시간 : 84