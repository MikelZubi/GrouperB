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