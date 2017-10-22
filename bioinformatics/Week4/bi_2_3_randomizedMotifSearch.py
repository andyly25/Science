# import the random package here
import random

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    # insert your code here
    # using our count function
    count = CountWithPseudocounts(Motifs)
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

# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    # insert your code here
    # sotre our random motif here
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
    # keep looping until score can go no higher
    while True:
        # grab our pseudo profile
        Profile = ProfileWithPseudocounts(M)
        # now grab our most probably motif
        M = Motifs(Profile, Dna)
        # now check if current best is less than best
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else: 
            return BestMotifs

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
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

def PrNew(Text, Profile):
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

def profileMostProbableNew(Text, k, Profile):
    # Set the initial result to be the first k-mer we check in case all values are under 0
    finalResult = Text[0:k]
    # print(finalResult)
    # initialize our max value var
    maxValue = 0
    # we loop through len of text minus k
    for i in range(len(Text) - k + 1):
        # Here we grab a k-mer to test
        textChunk = Text[i:i+k]
        # We run that kmer through our Pr function
        result = PrNew(textChunk, Profile)
        # so if the results is greater
        if result > maxValue:
            # we take that as out best kmer and continue comparing for max
            maxValue = result
            finalResult = textChunk
    return finalResult

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs = []
    k = len(Profile['A'])
    for dna in Dna:
        probKmer = profileMostProbableNew(dna, k, Profile)
        motifs.append(probKmer)
    return motifs

def main():
    k = 8 
    t = 5
    Dna = [
        "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    ]
    print(RandomizedMotifSearch(Dna, k, t))

    Dna2 = [
        "TGACGTTC",
        "TAAGAGTT",
        "GGACGAAA",
        "CTGTTCGC"
    ]
    k = 3
    t = len(Dna2)
    print(RandomizedMotifSearch(Dna2, k, t))

    Dna3 = [
        "TGA",
        "GTT",
        "GAA",
        "TGT"
    ]
    k = 3
    t = len(Dna3)
    print(RandomizedMotifSearch(Dna2, k, t))

if __name__ == '__main__':
    main()