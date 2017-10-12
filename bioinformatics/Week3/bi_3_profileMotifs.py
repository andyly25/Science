# Insert your Count(Motifs) function here from the last Code Challenge.
from bi_3_countMotif import Count


# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    # insert your code here
    # set profile equal to Count motifs
    profile = Count(Motifs)
    # we loop through length of the motif (moving horizontally)
    for i in range(k):
        # loop through each symbol (start from going top to bottom A, C, G, T)
        for symbol in "ACGT":
            # We now devide each element by t, number of rows of rows
            profile[symbol][i] = profile[symbol][i]/t
    return profile

# # Here's what someone else did
# def Profile(Motifs):
#     profile = Count(Motifs)
#     # looping through using key, values
#     for key, value in profile.items():
#         # goes through each elements divide by len(Motifs) or t and store as array to each key value
#         profile[key] = [x/len(Motifs) for x in profile[key]]
#     return profile


def main():
    Motifs = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]
    print(Profile(Motifs))
    # Output should be: 
    # {'A': [0.2, 0.4, 0.2, 0.0, 0.0, 0.4], 
    # 'C': [0.4, 0.2, 0.8, 0.4, 0.0, 0.0], 
    # 'G': [0.2, 0.2, 0.0, 0.4, 0.2, 0.2], 
    # 'T': [0.2, 0.2, 0.0, 0.2, 0.8, 0.4]}

if __name__ == '__main__':
    main()