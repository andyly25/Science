# Gibbs Sampling
- A more iterative algorithm compared to random motif search we made.
    - discards a single kmer from current set of motifs at each iteration 
    - decides to keep or replace with new one
    - moves with mroe caution in space of all motifs
    - ![random vs gibs](http://bioinformaticsalgorithms.com/images/Motifs/randomized_vs_gibbs.png "from stepik.org gibs vs random")
- starts with randomly chosen kmers in each t DNA strings
    - but makes a *random* choice at each iteration.
    - uses list t randomly selected kmer motifs to come up with another set kmers
    - randomly selects int i between 0 and t-1 and randomly changes a single kmer motif[i]
- Note: there will be a problem with 0's again so we have to use pseudocounts once again
- GibbsSampler may converge to a suboptimal solution
    - especially for difficult search problems with elusive motifs
- **local optimum**: solution optimal within small neighboring solutions
    - since gibbs explores a small subset of solutions, may get stuck
    - thus should be ran many times in hopes of an optimal
- **global optimum**: optimal solution among all possible solution
___

## Detour Complications in Motif Finding
- difficult if the **background nucleotide distribution** in sample is skewed
    - so a relevant motif can lose out to some other motif
- Another complication is that many motifs are represented in different alphabet than the alpha of 4 nucleotides
    - e.g.:  Let W denote either A or T, S denote either G or C, K denote either G or T, and Y denote either C or T
        - consider "CSKWYWWATKWATYYK", which represents the CSRE motif in yeast
        - This strong motif in hybrid motif corresponfs to 211 different motifs in standard 4 letter alphabet 