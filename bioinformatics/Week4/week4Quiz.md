# Week 4 Quiz:
1. True or False: it is not possible for GibbsSampler to move from a collection of motifs with lower score to a collection of motifs with higher score.
    - False
- True or False: RandomizedMotifSearch and GibbsSampler are usually run on only one choice of initial k-mers.
    - False
- True or False: RandomizedMotifSearch performs well when given a uniform profile matrix.
    - False
- True or False: it is not possible for RandomizedMotifSearch to move from a collection of motifs with lower score to a collection of motifs with higher score.
    - True
2. Which of the following motif-finding algorithms is guaranteed to find an optimum solution? In other words, which of the following are not heuristics? (Select all that apply.)
    - GreedyMotifSearch (with pseudocounts) x
    - BruteForceMotifSearch
    - RandomizedMotifSearch x
    - GreedyMotifSearch (without pseudocounts) x
    - GibbsSampler x
3. Assume given following string Dna:
    `"ATGAGGTC",
    "GCCCTAGA",
    "AAATAGAT",
    "TTGTGCTA"`
    - Then assume RandomizedMotifSearch begins by randomly choosing the following 3-mers Motifs of Dna:
    `"GTC",
    "CCC",
    "ATA",
    "GCT"`
    - What are the 3-mers after one iteration of RandomizedMotifSearch? In other words, what are the 3-mers Motifs(Profile(Motifs), Dna)? Please enter your answer as four space-separated strings.
        - GTC GCC ATA GCT
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
- Randomized algorithms that are not guaranteed to return exact solutions, but do quickly find approximate solutions, are named after the city of (blank).
    - Monte Carlo
6. Given the following "un-normalized" set of probabilities (i.e., that do not necessarily sum to 1):
    - 0.15 0.6 0.225 0.225 0.3
    - What is the normalized set of probabilities? (Enter your answer as a sequence of space-separated numbers.)
        - 0.1 0.4 0.15 0.15 0.2
    - {'1': 0.22, '2': 0.54, '3': 0.58, '4': 0.36, '5': 0.3 }
        - 0.11 0.27 0.29 0.18 0.15
    - {'1': 0.45, '2': 0.63, '3': 0.09, '4': 0.27, '5': 0.36 }
        - 0.25 0.35 0.05 0.15 0.2

### 8 tries later I finally got 100%
- kept getting tripped over from small variations of true and false
- the coding parts made small errors in entering data
    - results may go out of order so I had to manualy type in order for answer
    