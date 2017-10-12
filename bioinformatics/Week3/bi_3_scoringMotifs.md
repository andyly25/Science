# Scoring Motifs
- From motifs to profile matrices and consensus strings
    - Computational problem formulation would be to score individual instances of motifs depending how similar to "ideal" motif
        - Problem: we don't know the "ideal".
            - Attempt to select a k-mer for each string and score these k-mers depending how similar to each other
            - to define scoring, consider list of t DNA strings Dna, each string len n.
                - select a k-mer from each string to form collection motifs represented as t x k motif matrix
                - ![NF-kB binding sites form 10x12 matrix](http://bioinformaticsalgorithms.com/images/Motifs/nfkb.png "from stepik.org")
                - NF-kB binding sites form 10x12 matrix, with most frequent in upper case letters
                    - Python represent motif matrix as a list of strings motifs
                        - access ith string by motifs[i] and j by motifs[i][j]
                    - goal is to select k-mers resulting in the most "conserved" motif matrix

___

## Detour: Motif Scoring Functions
- For many biological motifs, certain positions feature 2 nucleotides with roughly same ability to bind to a transcription factore.
    - e.g. the sixteen nucleotide-long CSRE transcription factor binding site in the yeast S. cerevisiae consists of five strongly conserved positions in addition to eleven weakly conserved positions
    - ![yeast motif score](http://bioinformaticsalgorithms.com/images/Motifs/CSRE_motif.png "from stepik.org yeast motif score")
    - Note: every column of Profile(Motifs) corresponds to a **probability distribution**
        - collection of non negative numbers that sum to 1
        - **Entropy** is a measure of the uncertainty of a probability distribution (p<sub>1</sub>,..., p<sub>N</sub>)
            - you can Google the formula yourself
        - we apply the entropy formula over the probabilities of A, C, G, and T and we can get some nice data
        - In general, the more conserved the column, the smaller its entropy
            - so entropy useful method of scoring motif matrices 
            - the lower the entropy, the higher the information content

___

## Scoring motif continued
- For given choice of Motifs, cwe can construct a 4 x k count matrix
    - counts # of occur. of each nucleotides in each colulmn of matrix
    - element (i, j) of Count(Motifs) stores # times nucleotides i appears in col j Motifs
    - One way representing in Python is create list for each row in matrix and then organize into larger dictionary
    - ![count motif](http://bioinformaticsalgorithms.com/images/Motifs/count_matrix.png "from stepik.org count motif pic")

```python
count = {"A": [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0],
         "C": [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6],
         "G": [0, 0,10,10, 9, 9, 1, 0, 0, 0, 0, 0],
         "T": [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4]
        } 
```
- Code for Count(Motif) in bi_3_countMotif.py
- By dividing all the elements in matrix by number of rows we get a profile matrix.
![motifs, score, count, profile](http://bioinformaticsalgorithms.com/images/Motifs/motifs_score_count_profile.png "from stepik.org") 
- We can generate Count(Motifs) in order to compute Profile(Motifs)
    - divide each element of count matrix by num of rows in couunt matrix
    - Code is in `bi_3_profileMotifs.py`
- With profile motifs we can now form a consensus string
    - from most popular nucleotides in each column of motifs matrix
    - if we select motifs from cllection of upstream regions 
        - it provides a candidate regulatory motif for these regions
    - can implement by using Count(motifs) as subroutine
        - note: jth symbol of consensus string is equal to symbol correspond max element in col j Count(Motifs)
        - code is in `bi_3_consensusMotifs.py`
- Now we can compute score motifs by constructing a consensus first
    - then summing num of symbols in j col that dont match symbols in j col of consensus
    - found in `bi_3_scoringMotifs.py`

___

# The Motiff Finding Problem
- Motif Finding Problem:  Given a collection of strings, find a set of k-mers, one from each string, that minimizes the score of the resulting motif. 
    - Input: Collection of strings Dna and an integer k
    - Output: A collection of Motifs of k-mers, one from each string Dna, minimizing Score(Motifs) among all possible choices of k-mers
- **Brute force search** (AKA exhaustive search) is a general problem solving exploring all possible candidate solutions 
    - checks if each candidate will solve the problem
    - This method will probably take literally forever
- benchmark our motif finding algorithms by using a **Subtle Motif Porblem**
    - refers to implanting a 15 mer with 4 random mutations in 10 randomly generated 600 nucleotide long strings
- Runtime of Brute force
    - There are n-k+1 choices of k0mers in each t strings so.. (n-k+1)<sup>t</sup> different ways to form motifs
    - each choice Motifs we calculate Score(Motifs) taking kxt steps
    - Thus, assuming k smaller than n, run time is ((n-k+1)<sup>t</sup>) x k x t
        - for subtle motif problem this is on order of 10<sup>29</sup> steps
    - We have assumed k is known in advance, but this not the case in practice
        - so we are forced to run for different values of k and deduce correct motif length
