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
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            p = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, p))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs

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