import bisect
import sys
input = sys.stdin.readline

li = []
while True:
    try:
        bisect.bisect_left(li,int(input()))
    except:
        while li:
            