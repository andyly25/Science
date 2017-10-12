# Insert your Count(Motifs) function here.
from bi_3_countMotif import Count

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


def main():
    Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    print(Consensus(Motifs))

if __name__ == '__main__':
    main()