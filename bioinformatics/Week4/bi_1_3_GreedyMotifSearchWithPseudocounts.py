# This was literally a copy and paste with some renaming of functions

# Copy your GreedyMotifSearch function (along with all required subroutines) from Motifs.py below this line
# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
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

# Input:  A set of kmers Motifs
# Output: Count(Motifs)
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

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
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

# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
# some profile probability function thing
def Pr(Text, Profile):
    # sets to 1 since we are multiplying into it, if it was 0... well we get nowhere
    result = 1
    # loop through len of text
    for i in range(len(Text)):
        # we grab the letter to use to find specific elements
        letter = Text[i]
        # now as we loop through we just mutiply the letter and position we are currently in string
        result *= Profile[letter][i]
    # we get our results w
    return result


# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
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
        result = Pr(textChunk, Profile)
        # so if the results is greater
        if result > maxValue:
            # we take that as out best kmer and continue comparing for max
            maxValue = result
            finalResult = textChunk
    return finalResult

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    # type your GreedyMotifSearch code here.
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            p = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, p))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

    return BestMotifs

def main():
    # Copy the ten strings occurring in the hyperlinked DosR dataset below.
    Dna = [
    "GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
    "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
    "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", 
    "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
    "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", 
    "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", 
    "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", 
    "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", 
    "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", 
    "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"
    ]

    # set t equal to the number of strings in Dna and k equal to 15
    t = len(Dna)
    k = 15

    # Call GreedyMotifSearchWithPseudocounts(Dna, k, t) and store the output in a variable called Motifs
    Motifs = GreedyMotifSearchWithPseudocounts(Dna, k, t)

    # Print the Motifs variable
    print(Motifs)

    # Print Score(Motifs)
    print(Score(Motifs))

if __name__ == '__main__':
    main()