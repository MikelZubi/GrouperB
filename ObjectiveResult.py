import copy as cp

def result(x,y):
    xy = cp.deepcopy(x)
    for i in range(0,len(xy)):
        for j in range(0,len(xy[i][:])):
            xy[i][j] = y[int(x[i][j])]
    counter = []
    perf = sum(y)/len(xy)
    for i in range(0,len(xy)):
        counter.append(abs(sum(xy[i][:])-perf))
    return sum(counter)

def resultV(x,y,n):
    perf = sum(y)/n
    value = [0 for i in range(n)]
    for i in range(len(y)):
        value[x[i]]+=y[i]
    counter = 0
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