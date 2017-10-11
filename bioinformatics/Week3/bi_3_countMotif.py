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

# My version with ordered dictionary, Note: a regular dictionary doesn't have order
# # Input:  A set of kmers Motifs
# # Output: Count(Motifs)
# from collections import OrderedDict
# def Count(Motifs):
#     count = OrderedDict() # initializing the count dictionary
#     # your code here
#     k = len(Motifs[0])
#     for symbol in "ACGT":
#         count[symbol] = []
#         for j in range(k):
#             count[symbol].append(0)
#     t = len(Motifs)
#     for i in range(t):
#         for j in range(k):
#             symbol = Motifs[i][j]
#             count[symbol][j] += 1
#     return count


def main():
    Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    print(Count(Motifs))

if __name__ == '__main__':
    main()

