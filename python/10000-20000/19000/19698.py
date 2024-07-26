n,w,h,l = map(int,input().split())
l = (w//l)*(h//l)
print(min(n,l))