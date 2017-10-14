from bi_3_countMotif import Count
from bi_3_profileMotifs import Profile
from bi_3_scoringMotifs import Score
from bi_3_consensusMotifs import Consensus
from bi_4_exercistBreak import Pr
from bi_4_profileMostProbable import ProfileMostProbablePattern

# Wow... this used pretty much everything... I'll backtrack this program tomorrow.

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    # type your GreedyMotifSearch code here.
    # Starts by setting best motifs equal to 1st kmer from each string in Dna
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    # then ranges over all possible k-mers in Dna[0]
    for i in range(n-k+1):
        # starts building a profile matrix for lone k-mer
        Motifs = []
        # sets motifs[1] equal to profile most probable k-mer in Dna[1]
        Motifs.append(Dna[0][i:i+k])
        # iterates by updating profile as profile matrix formed from motifs[0] and motifs[1]
        # then setting motifs[2] = Profile most probable k-mer in Dna[2]
        # tldr: after finding k-mer motifs in first i-string dna, we contruct Profile and set Motifs[i] = Profile most probable kmer
        for j in range(1, t):
            p = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, p))
        # so if the current motifs outscores the current best scoring motif, it is now the new Bestmotifs
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    # after looping through and generating a collection Motiffs for every possible initial k-mer from Dna[0], returns all the high scorers
    return BestMotifs

def main():
    Dna = [
        "GGCGTTCAGGCA", 
        "AAGAATCAGTCA", 
        "CAAGGAGTTCGC",
        "CACGTCAATCAC", 
        "CAATAATATTCG"
    ]

    print(GreedyMotifSearch(Dna, 3, 5))

if __name__ == '__main__':
    main()