import DataStructure as dt
import BruteForce as bt
import backtrack as btr
import time
import GeneticAlgorithm as ga
import ObjectiveResult as result
import for2 as f2



struct2 = dt.Structure(2,"Proof/ProofG.txt","Proof/ProofGNames.txt")
#struct2.randomInitialization()
#struct2.print()
a = float(time.time())
struct2.updateX(f2.linearProgramming(struct2.y))
struct2.print()
b = a - float(time.time())
print(b)
'''
a = float(time.time())
struct2.updateX(bt.BruteForce(struct2.y,struct2.n))
struct2.print()
b = a - float(time.time())
print(b)
a = float(time.time())
struct2.updateX(btr.init(struct2.y,struct2.n))
struct2.print()
b = a - float(time.time())
print(b)
'''
a = float(time.time())
struct2.updateX(ga.geneticAlgorithm(struct2.y,struct2.n,500))
struct2.print()
b = a - float(time.time())
print(b)