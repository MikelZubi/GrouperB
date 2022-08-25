import random as rd
import ObjectiveResult as result

def geneticAlgorithm(y,n,p):
    pob = [[rd.choice([i for i in range(n)]) for i in range(len(y))] for i in range(p)]
    #Per generation 20% worst individuals will be replaced by the next generations individuals
    #Because of that 40% will need to get a child.
    best = [-1 for i in range(int(p * 0.4))]
    worst = [-1 for i in range(int(p * 0.2))]
    finish = False
    count = 0
    while count<=50000 and not finish:
        results = [result.resultV(pob[i],y,n) for i in range(p)]
        min = float('inf')
        for j in range(len(results)):
            if (min > results[j]):
                min = results[j]
        print("GENERATION ", count)
        print("VALUE ", min)
        if (min == 0.0):
            break
        for i in range(len(best)):
            min = float('inf')
            minp = -1
            for j in range(len(results)):
                if(min > results[j] and not j in best):
                    min = results[j]
                    minp = j
            best[i] = minp
        for i in range(len(worst)):
            max = 0
            maxp = -1
            for j in range(len(results)):
                if(max < results[j] and not j in worst):
                    max = results[j]
                    maxp = j
            worst[i] = maxp
        for i in range(len(worst)):
            pob[worst[i]] = ugaldu(pob[best[i]],pob[best[i*2]],n)
        count += 1
        conb = conbergetion(pob, n)
        finish = all(conb)
        print("CONVERGED ", conb.count(True))
    results = [result.result(translator(pob[i], n), y) for i in range(p)]
    min = float('inf')
    minp = -1
    for j in range(p):
        if (min > results[j]):
            min = results[j]
            minp = j
    return translator(pob[minp],n)


def ugaldu(x1, x2, n):
    x3 = []
    for i in range(len(x1)):
        mut = rd.randint(0, 100)
        if (mut >= 98 and (n>2 or x1[i] == x2[i])):
            r = [j for j in range(n) if j != x1[i] and j != x2[i]]
        else:
            r = [x1[i], x2[i]]
        gen = rd.choice(r)
        x3.append(gen)
    return x3

def translator(x,n):
    xn = [[]for elem in range(n)]
    for i in range(len(x)):
        xn[x[i]].append(i)
    return xn

def conbergetion(pob,n):
    converged = [False for i in range(len(pob[0]))]
    for j in range(len(pob[0])):
        values = [0 for i in range(n)]
        for i in range(len(pob)):
            values[pob[i][j]]+= 1
        for elem in values:
            if elem/len(pob) > 0.95:
                converged[j] = True
                break
    return converged



