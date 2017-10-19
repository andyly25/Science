# import Python's 'random' module here
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

def main():
    k = 3
    t = 5
    Dna = [
        "TTACCTTAAC",
        "GATGTCTGTC",
        "ACGGCGTTAG",
        "CCCTAACGAG",
        "CGTCAGAGGT"
    ]
    print(RandomMotifs(Dna, k, t))

if __name__ == '__main__':
    main()