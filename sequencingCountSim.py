# a simple model to work out how many sequencing reactions we would have to do to have a certain % certainty 
# of having at least one babblebrick from a gblock of n babblebricks
# babbled - edinburgh ug igem 2016
#freddie starkey

from itertools import product
import matplotlib.pyplot as plt

def plotOut(noReactions):
    plt.plot(range(1, noReactions + 1), [simMain(2, reactionCount) for reactionCount in xrange(1, noReactions + 1)], 'b-', label="2 words per gBlock")
    plt.plot(range(1, noReactions + 1), [simMain(3, reactionCount) for reactionCount in xrange(1, noReactions + 1)], 'r-', label="3 words per gBlock")
    plt.plot(range(1, noReactions + 1), [simMain(4, reactionCount) for reactionCount in xrange(1, noReactions + 1)], 'g-', label="4 words per gBlock")
    plt.plot(range(1, noReactions + 1), [simMain(5, reactionCount) for reactionCount in xrange(1, noReactions + 1)], 'k-', label="5 words per gBlock")
    plt.xlabel("number of sequencing reactions")
    plt.ylabel("accuracy (%)")
    plt.legend()
    plt.show()

def simMain(noInGBlock, noReactions):
    miss = 0.0
    table = list(product(range(0, noInGBlock), repeat=noReactions))
    total = float(len(table))
    for eachPerm in table:
        if checkAllPresent(eachPerm, noInGBlock) == False:
            miss = miss + 1
    return 1.0 - miss/total

def checkAllPresent(eachPerm, noInGBlock):
    for eachWord in range(0, noInGBlock):
        if eachWord not in eachPerm:
            return False
    return True
