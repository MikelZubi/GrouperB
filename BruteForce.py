import copy as cp
import ObjectiveResult as result


def BruteForce(y,n):
    p = [0 for i in y]
    l = n-1
    last = [l for i in y]
    best = kalkulatuIter(p,y,n)
    bestp = p
    while p != last:
        for i in reversed(range(len(p))):
            if(p[i] != l):
                p[i] += 1
                e = kalkulatuIter(p,y,n)
                print(p)
                if(best > e):
                    best = e
                    bestp = cp.deepcopy(p)
                break
            else:
                p[i] = 0
    return getX(bestp,n)

def kalkulatuIter(p,y,n):
    x = [[]for i in range(n)]
    for i in range(0,len(p)):
        x[p[i]].append(i)
    return result.result(x,y)

def getX(p,n):
    x = [[] for i in range(n)]
    for i in range(0, len(p)):
        x[p[i]].append(i)
    return x


