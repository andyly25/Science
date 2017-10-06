# Trying another method, apparently voted as best method if not dealing with packages
from sys import path as syspath
from inspect import currentframe as currframe, getfile as getfile
from os.path import dirname as osdirname, abspath as osabspath  
currentdir = osdirname(osabspath(getfile(currframe())))
parentdir = osdirname(currentdir)
syspath.insert(0, parentdir)

# # This is a shorter form someone made of the above
# sys.path.insert(1, os.path.join(sys.path[0], '..'))

# We did all the above so we can access files from the parent directory!
from Week1.bi2_2_patternCount import PatternCount 

# A more efficient version
def FasterSymbolArray(Genome, symbol):
    array = {}
    # grabbing length of genome
    n = len(Genome)
    # This is the genome including the half added at the end
    ExtendedGenome = Genome + Genome[0:n//2]
    # our first array is a count of how many times our symbol appears in that half
    array[0] = PatternCount(symbol, Genome[0:n//2])
    # now we start sliding at pos 1
    for i in range(1, n):
        # We want array to start at 0 so we subtract by 1 since we started at 1
        array[i] = array[i - 1]
        # if the first letter is a symbol, it's going to disappear when we slide so we subtract 1
        if ExtendedGenome[i - 1] == symbol:
            # could shorten to -= 1
            array[i] = array[i] - 1
        # if the end is the symbol, we add 1 since it will now be part of our window.
        if ExtendedGenome[i + (n//2) - 1] == symbol:
            # could shorten to += 1
            array[i] = array[i] + 1
    return array