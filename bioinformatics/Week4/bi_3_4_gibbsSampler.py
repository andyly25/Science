# first, import the random package
import random

# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    motifs = []
    for dna in Dna:
        # note positions of arrays starts at 0, and - k since we don't want to go over 
        randomPos = random.randint(0, len(dna)-k)
        # now we append into our motifs list
        motifs.append(dna[randomPos: randomPos+k])
    return motifs

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    # set profile equal to Count motifs
    profile = CountWithPseudocounts(Motifs)
    # we loop through length of the motif (moving horizontally)
    for i in range(k):
        # loop through each symbol (start from going top to bottom A, C, G, T)
        for symbol in "ACGT":
            # We now divide each element by t, number of rows of rows
            # Add 4 I guess since there's 4 symbols and we need add 1 for each column
            profile[symbol][i] = profile[symbol][i]/(t+4)
    return profile

def CountWithPseudocounts(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    # we grab the len of one of our Motif values
    k = len(Motifs[0])
    # Now we loop through each ont of the protein symbols
    for symbol in "ACGT":
        # initialize a list for each symbol
        count[symbol] = []
        # append a 1 for each element in the matrix, this will be our pseudocounts
        for j in range(k):
            count[symbol].append(1)

    # Now we grab len of how many motifs we have
    t = len(Motifs)
    # loop through that length
    for i in range(t):
        # now go through len of K again
        for j in range(k):
            # grab the symbol for that matrix
            symbol = Motifs[i][j]
            # increment by 1 for that symbol
            count[symbol][j] += 1
    return count

# then, copy Pr, Normalize, and WeightedDie below this line
def Pr(Text, Profile):
    # sets to 1 since we are multiplying into it, if it was 0... well we get nowhere
    result = 1
    # loop through len of text
    for i in range(len(Text)):
        # we grab the letter to use to find specific elements
        letter = Text[i]
        # now as we loop through we just mutiply the letter and position we are currently in string
        result *= Profile[letter][i]
    # we get our results with a lot decimals if not 0
    return result

# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    # make a empty dict to store what we want
    newDict = {}
    # grab sum of all values
    probSum = sum(Probabilities.values())
    # iterating through keys and values of Probabilities..
    # forgot to have the .items() at end and wondered why didnt work
    for k, v in Probabilities.items():
        # store new values with the values/sum
        newDict[k] = v/probSum
    # return our results
    return newDict

    # Here's a one line version
    # return {key : probabilities[key] / sum(probabilities.values()) for key in probabilities}

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    # grabbing sum to use
    totsum = 0
    # grabbing a random value between 0 and 1
    randVal = random.uniform(0, 1)
    # print("randval is " + str(randVal))
    # now we loop through the key and values
    for k, v in Probabilities.items():
        # continue updating the total sum with values
        totsum += v
        # if our random value is < totsum, then current k is our kmer
        if randVal < totsum:
            kmer = k
            break
    return kmer


# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    # grab len text and making a blank dictionary
    n = len(Text)
    probabilities = {}
    # now range over all possible kmers in Text
    for i in range(0, n-k+1):
        # compute probability of each one and placing probability into a dictionary
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    # then normalize the probabilities
    probabilities = Normalize(probabilities)
    # and return result of rolling a weighted die
    return WeightedDie(probabilities)

# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    count = {} # initializing the count dictionary
    # your code here
    # we grab the len of one of our Motif values
    k = len(Motifs[0])
    # Now we loop through each ont of the protein symbols
    for symbol in "ACGT":
        # initialize a list for each symbol
        count[symbol] = []
        # append a 0 for each element in the matrix
        for j in range(k):
            count[symbol].append(0)

    # Now we grab len of how many motifs we have
    t = len(Motifs)
    # loop through that length
    for i in range(t):
        # now go through len of K again
        for j in range(k):
            # grab the symbol for that matrix
            symbol = Motifs[i][j]
            # increment by 1 for that symbol
            count[symbol][j] += 1
    return count

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    # insert your code here
    # using our count function
    count = Count(Motifs)
    # grab the length of a single motif
    k = len(Motifs[0])
    consensus = ""
    # now we loop through the length of a motif
    for j in range(k):
        # initialize max value to be 0
        m = 0
        # a value to store most frequent symbol
        frequentSymbol = ""
        # now we go through each of the symbols for each column
        for symbol in "ACGT":
            # so if an element is >m 
            if count[symbol][j] > m:
                # we set that new value to be max
                m = count[symbol][j]
                # and make that symbol our most frequent
                frequentSymbol = symbol
        # now after finishing the column we add it to our string
        consensus += frequentSymbol
    return consensus

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    # Insert code here
    # grab our consensus data
    consensus = Consensus(Motifs)
    # length of a motifs
    k = len(Motifs[0])
    # number of rows
    t = len(Motifs)
    # init score to 0
    score = 0
    # loop horizontally along the motif
    for j in range(k):
        # loop vertically for all the symbols
        for el in range(t):
            # if symbol does not matche the consenseus we increment 1
            if Motifs[el][j] != consensus[j]:
                score += 1
    # return the score
    return score

'''
Here's the pseudocode of what I was supposed to do.

GibbsSampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        ﻿BestMotifs ← Motifs
        for j ← 1 to N
            i ← randomly generated integer between 1 and t
            Profile ← profile matrix formed from all strings in Motifs except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th string
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
'''

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    # your code here
    motifs = RandomMotifs(Dna, k, t)
    BestMotifs = motifs
    for j in range(N):
        i = random.randint(0, t-1)
        removed = motifs.pop(i)
        profile = ProfileWithPseudocounts(motifs)
        motifs.insert(i, ProfileGeneratedString(removed, profile, k))
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs


# .... apparently all my errors was from forgetting commas in Dna..
# Could have been done with this 2 hours earlier
def main():
    # Copy the ten strings occurring in the hyperlinked DosR dataset below.
    Dna =["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", 
    "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", 
    "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", 
    "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", 
    "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", 
    "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", 
    "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", 
    "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", 
    "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", 
    "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

    # set t equal to the number of strings in Dna, k equal to 15, and N equal to 100
    t = len(Dna)
    k = 15
    N = 100

    # Call GibbsSampler(Dna, k, t, N) 20 times and store the best output in a variable called BestMotifs
    BestMotifs = RandomMotifs(Dna, k, t)
    for i in range(20):
        M = GibbsSampler(Dna, k, t, N)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M

    # Print the BestMotifs variable
    print(BestMotifs)
    # Print Score(BestMotifs)
    print(Score(BestMotifs))

if __name__ == '__main__':
    main()
