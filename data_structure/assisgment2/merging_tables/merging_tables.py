# python3

import sys

n, m = map(int, sys.stdin.readline().split())
#org_lines = list(map(int, sys.stdin.readline().split()))
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans=[]
ans.append(max(lines))

def getParent(i):
    # find parent and compress path
    if i!=parent[i]:
        parent[i]=getParent(parent[i])

    return parent[i]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination==realSource:
        ans.append(lines[realSource])
        #print (max(ans))
    else:
        lines[realDestination]=lines[realSource]+lines[realDestination]
        parent[realSource]=realDestination

    print(max(lines))


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    #print(ans)
    
