# Note you can uncomment some of the test prints I commented out to test

# using regular expressions
import re

# count occurence of the pattern in a string
def patternCount(pattern, string):
    return len(re.findall("(?=%s)"%pattern, string))

# results shall be printed
# print(patternCount("ACTAT", "ACAACTATGCATACTATCGGGAACTATCCT"));


# Bit lazy so the for loop assignment shall also be here

# At what position would we stop sliding a 10-nucleotide window along a string of length 1000?

count = 0
# can grab length by: len(Text)
length = 1000
# can grab by: len(pattern)
kmer = 10
steps = 1
# a 10 length kmer sliding down 1 by 1 of a string lenght of 1000
for i in range(0, length - kmer, steps):
    count += 1

# it's pretty much 1000 - 10
# print(count)

# here's the instructors' function for this
# Copy your PatternCount function from the previous step below this line
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count

# Now, set Text equal to the ori of Vibrio cholerae and Pattern equal to "TGATCA"
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGA"
"TGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGA"
"TTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCC"
"AAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTA"
"GGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTT"
"ACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGA"
"CTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCT"
"CTTGATCATCGTTTC"

Pattern = "TGATCA"

# Finally, print the result of calling PatternCount on Text and Pattern.
# print(PatternCount(Pattern, Text))
# Don't forget to use the notation print() with parentheses included!

# Find the most frequent 2-mer of "GATCCAGATCCCCATAC". (You should solve this exercise by hand; how can it be done quickly?)
# Here's an adaptation of someone's solution
merLength = 2

def FindMer(Text):
    merList = []
    freqDict = {}
    # loop the length of the text
    for i in range(len(Text)-1):
        # so if our 2 mer is not found in the list
        if Text[i:i+merLength] not in merList:
            # we append that 2 char into the list
            merList.append(Text[i:i+merLength])
    # now we loop through the list we made
    for j in merList:
        # and we now add a key value pair of the 2 mer and occurence
        freqDict[j] = PatternCount(j,Text)
    # we now return the dictionary
    return freqDict 
# Print out the result
# print (FindMer("GATCCAGATCCCCATAC"))