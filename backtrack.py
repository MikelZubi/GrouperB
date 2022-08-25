import ObjectiveResult as res

best = float('inf')
bestX = []

def backtrack(y, x, n, p):
    global best
    global bestX
    if(p == len(y)-1):
        return res.resultV(x,y,n)
    #if()
    for i in range(n):
        x[p] = i
        lag = backtrack(y, x, n, p+1)
        if lag < best:
            best = lag
            bestX = translator(x,n)
    return best


def init(y, n):
    backtrack(y, [-1 for i in range(len(y))], n, 0)
    return bestX

def translator(x,n):
    xn = [[]for elem in range(n)]
    for i in range(len(x)):
        xn[x[i]].append(i)
    return xn

