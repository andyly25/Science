# Week 4 Quiz:
1. True or False: it is not possible for GibbsSampler to move from a collection of motifs with lower score to a collection of motifs with higher score.
    - False
2. Which of the following motif-finding algorithms is guaranteed to find an optimum solution? In other words, which of the following are not heuristics? (Select all that apply.)
    - GreedyMotifSearch (with pseudocounts) x
    - BruteForceMotifSearch
    - RandomizedMotifSearch x
    - GreedyMotifSearch (without pseudocounts) x
    - GibbsSampler 
3. Assume given following string Dna:
    `TGACGTTC
    TAAGAGTT
    GGACGAAA
    CTGTTCGC`
    - Then assume RandomizedMotifSearch begins by randomly choosing the following 3-mers Motifs of Dna:
    `TGA
    GTT
    GAA
    TGT`
    - What are the 3-mers after one iteration of RandomizedMotifSearch? In other words, what are the 3-mers Motifs(Profile(Motifs), Dna)? Please enter your answer as four space-separated strings.
        - TGA GTT CGA CTG
4. Given the following code in Python:
    ```python
        import random
        y=random.randint(1,10)
        if y>=1 and y < 3:
            print("A")
        elif y>=3 and y<=7:
            print("B")
        else: print("C")
    ```
    - What is the probability (represented as a decimal) that "B" will be printed?
        - 0.5
5. Randomized algorithms that produce solutions guaranteed to be exact are named after the city of (blank).
    - Las Vegas
6. Given the following "un-normalized" set of probabilities (i.e., that do not necessarily sum to 1):
    - 0.22 0.54 0.58 0.36 0.3
    - What is the normalized set of probabilities? (Enter your answer as a sequence of space-separated numbers.)
        - 0.29 0.18 0.11 0.27 0.15