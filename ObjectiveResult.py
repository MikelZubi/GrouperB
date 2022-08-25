import copy as cp

def result(x,y):
    xy = cp.deepcopy(x)
    for i in range(len(xy)):
        for j in range(len(xy[i][:])):
            xy[i][j] = y[x[i][j]]
    counter = 0.0
    perf = sum(y)/len(xy)
    for i in range(0,len(xy)):
        counter += abs(sum(xy[i][:])-perf)
    return counter

def resultV(x,y,n):
    perf = sum(y)/n
    value = [0 for i in range(n)]
    for i in range(len(y)):
        value[x[i]]+=y[i]
    counter = 0.0
    for i in range(n):
        counter += abs(value[i]-perf)
    return counter

def bigGroup(y,x,n):
    perf = sum(y) / n
    value = [0 for i in range(n)]
    for i in range(len(y)):
        value[x[i]] += y[i]
    for i in range(n):
        return value[i] >= perf + y[x.index(i)]