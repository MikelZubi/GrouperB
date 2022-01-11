import DataStructure as dt
import BruteForce as bt
import timeit
import ObjectiveResult as result

struct2 = dt.Structure(3,"Proof/Proof.txt","Proof/ProofNames.txt")
struct2.randomInitialization()
struct2.print()
struct2.updateX(bt.BruteForce(struct2.y,struct2.n))
t1 = timeit.default_timer()
struct2.print()
t2 = timeit.default_timer()
print("Denbora: ", t2-t1)
