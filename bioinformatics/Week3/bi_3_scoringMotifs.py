# Copy your Count(Motifs) function here.
# Copy your Consensus(Motifs) function here.

from bi_3_countMotif import Count
from bi_3_consensusMotifs import Consensus

# # Input:  A set of k-mers Motifs
# # Output: The score of these k-mers.
# def Score(Motifs):
#     # Insert code here
#     # grab our consensus data
#     consensus = Consensus(Motifs)
#     # length of a motifs
#     k = len(Motifs[0])
#     # number of rows
#     t = len(Motifs)
#     # init score to 0
#     score = 0
#     # loop horizontally along the motif
#     for j in range(k):
#         # loop vertically for all the symbols
#         for el in range(t):
#             # if symbol does not matche the consenseus we increment 1
#             if Motifs[el][j] != consensus[j]:
#                 score += 1
#     # return the score
#     return score


# # Here's what someone else did for theirs
# # The value of score is equal to the total number of motifs - the value of the consensus symbol on the i-th position
# def Score(Motifs):
#     score = 0
#     consensus = Consensus(Motifs)
#     count = Count(Motifs)
#     for i in range(len(consensus)):
#         score = score + len(Motifs) - count[consensus[i]][i]
#     return score  

def main():
    Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    print(Score(Motifs))

if __name__ == '__main__':
    main()