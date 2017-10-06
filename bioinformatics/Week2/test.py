# Still confused with the python package control and the __init__.py so leaving for another day
# apparently you can use .. to go up one parent, and ... go up 2 directories, but requires correct package settings

# # This method did not work
# from ..Week1.bi2_2_patternCount import PatternCount

# # This works, but using sys path is really not recommended
# import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # import ../db.py
# from Week1.bi2_2_patternCount import PatternCount

# # Let's look at the path it gives
# from os.path import dirname, abspath
# print(dirname(dirname(abspath(__file__))))


# Trying another method, apparently voted as best method if not dealing with packages
# note i added in my own aliases
from sys import path as sp
from inspect import currentframe as cf, getfile as gf
from os.path import dirname as odirname, abspath as oabspath  
currentdir = odirname(oabspath(gf(cf())))
parentdir = odirname(currentdir)
sp.insert(0, parentdir)

# # This is a shorter form someone made of the above
# sys.path.insert(1, os.path.join(sys.path[0], '..'))

from Week1.bi2_2_patternCount import PatternCount


Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGA"
"TGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGA"
"TTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCC"
"AAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTA"
"GGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTT"
"ACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGA"
"CTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCT"
"CTTGATCATCGTTTC"

Pattern = "TGATCA"

print(PatternCount(Pattern, Text))
