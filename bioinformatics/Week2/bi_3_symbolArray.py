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


# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
def SymbolArray(Genome, symbol):
    array = {}
    # type your code here
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

Genome = 'AAAAGGGG'
symbol = 'A'


# Here's the PatternCount as a refresher
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

# print(SymbolArray(Genome, symbol))

