x, y = map(int, input().split())
print("2", x * y - x, y - x * y, sep = "\n")
'''
import heapq

def solution(jobs):
    res = 0
    time = 0
    jobs0 = []
    jobs1 = []
    
    for job in jobs:
        heapq.heappush(jobs0, (job[0], job[1]))
    
    while jobs0 or jobs1:
        while jobs0 and jobs0[0][0] <= time:
            start, end = heapq.heappop(jobs0)
            heapq.heappush(jobs1, (end, start))
        
        if not jobs1:
            time = jobs0[0][0]
        else:
            end, start = heapq.heappop(jobs1)
            time += end
            res += (time - start)
    
    return res // len(jobs)
'''

'''
from collections import deque

def solution(points, routes):
    maps = [[set() for _ in range(101)] for _ in range(101)] 
    meets = 0
    meet = 
    d = ((0,1),(0,-1),(-1,0),(1,0),)

    for route in routes:
        times = 1
        for p in range(0,len(route),2):
            q = deque()
            y,x = points[route[p] - 1]
            fy,fx = points[route[p + 1] - 1]
            visit = set([(y,x)])
            q.append((y,x,times,[(y,x,times)]))

            while q:
                y,x,time,rec = q.popleft()
                if y == fy and x == fx:
                    break
                for dy,dx in d:
                    dy += y
                    dx += x
                    if 0 < dy < 101 and 0 < dx < 101:
                        if (dy,dx) in visit:
                            continue
                        visit.add((dy,dx))
                        trec = rec
                        trec.append((dy,dx,time + 1))
                        q.append((dy,dx,time + 1,rec))
            times += time                  
            for y,x,time in rec:
                if time in maps[y][x]:
                    print(y,x,time)
                    meets += 1
                else:
                    maps[y][x].add(time)        
    return meets

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [2, 4]]
print(solution(points,routes))
'''