
import random as rd
import NPermutation
import ObjectiveResult as result
import copy as cp


class Structure:
    def __init__(self,n,Ytxt,Nametxt):
        self.n = n
        self.Ytxt = Ytxt
        self.Nametxt = Nametxt
        f = open(Ytxt, "r")
        y = []
        for x in f:
            j = 0
            l = []
            for w in x.split():
                y.append(float(w))
        self.y = y
        self.x = None
        self.xNames = None
        self.xY=None

    def ordinaryInitialization(self):
        x = [[]for i in range(self.n)]
        for i in range(0,len(self.y)):
            x[0].append(i)
        print(x)
        self.x = x
        self.__updateXNames()
        self.__updateXY()

    def randomInitialization(self):
        ry = rd.sample(range(len(self.y)),len(self.y))
        rx = [[] for i in range(self.n)]
        for i in ry:
            g = rd.randint(0, (self.n-1))
            rx[g].append(i)
        print(rx)
        self.x = rx
        self.__updateXNames()
        self.__updateXY()

    def print(self):
        print()
        print("n = " + str(self.n))
        print("Nº of permutation >= " + str(NPermutation.getNPermutation(self.n,len(self.y))))
        print("Ytxt: " + self.Ytxt)
        print("NameTxt: " + self.Nametxt)
        print("Y:")
        print(self.y)
        print("X:")
        print(self.x)
        print("XName: ")
        print(self.xNames)
        print("Xy: ")
        print(self.xY)
        print("Value: ")
        print(result.result(self.x,self.y))
        print()
    def updateX(self,x):
        self.x = x
        self.__updateXNames()
        self.__updateXY()
    def __updateXNames(self):
        f = open(self.Nametxt,"r")
        yN = []
        for h in f:
            for w in h.split():
                yN.append(w)
        xN = cp.deepcopy(self.x)
        for i in range(0,len(xN)):
            for j in range(0,len(xN[i][:])):
                xN[i][j] = yN[int(self.x[i][j])]
        self.xNames = xN
    def __updateXY(self):
        y = self.y
        x = self.x
        xy = cp.deepcopy(x)
        for i in range(0, len(x)):
            for j in range(0, len(x[i][:])):
                xy[i][j] = y[int(x[i][j])]
        self.xY = xy

