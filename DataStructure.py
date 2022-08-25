
import random as rd
import NPermutation
import ObjectiveResult as result
import copy as cp


#Hobena ordenazioak hemen bertan sartzea beharbada hasierako izenak jaso eta y-ren orden berrian arabera ber-ordenatu
#Ola izenak jasota daudela x-ek adierazten dun taldean sartzea izango zen bakarrik.
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
        self.y, self.xV = self.__mergeSort(y,[i for i in range(len(y))],n)
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

    def __mergeSort(self, y, x):
        if len(y) > 1:
            mid = len(y) // 2
            lefty = y[:mid]
            righty = y[mid:]
            leftx = x[:mid]
            rightx = x[mid:]

            # Recursive call on each half
            self.__mergeSort(lefty, leftx)
            self.__mergeSort(righty, rightx)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            while i < len(lefty) and j < len(righty):
                if lefty[i] <= righty[j]:
                    # The value from the left half has been used
                    y[k] = lefty[i]
                    x[k] = leftx[i]
                    # Move the iterator forward
                    i += 1
                else:
                    y[k] = righty[j]
                    x[k] = rightx[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(lefty):
                y[k] = lefty[i]
                x[k] = leftx[i]
                i += 1
                k += 1

            while j < len(righty):
                y[k] = righty[j]
                x[k] = rightx[j]
                j += 1
                k += 1
        return y, x
