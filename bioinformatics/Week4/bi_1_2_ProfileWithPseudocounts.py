from bi_1_1_CountWithPseudocounts import CountWithPseudocounts

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

def main():
    Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    print(ProfileWithPseudocounts(Motifs))

if __name__ == '__main__':
    main()