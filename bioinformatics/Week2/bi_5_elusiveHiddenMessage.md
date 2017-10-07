# Some hidden messages are more elusive than others
- Solving min skew problem gave us location of ori at 3923620 in E.Coli
    - now we go in and check using our frequentWords function with windows length 500
    - Problem: no 9-mers (including complements) appearing 3 or more times
        - going back to ori of Vibrio cholerae noticed that along with:
            - three occurrences of ATGATCAAG and three occurrences of its reverse complement CTTGATCAT
            - contains additional occurrences of ATGATCAA**C** and C**A**TGATCAT
                - differ by 1 nucleotide
                - And we recall that DnaA can bind to both "perfect" and also their slight mutation versions
___

## Hamming Distance Problem: Compute the Hamming distance between two strings. 
- Input: Two strings of equal length.
- Output: The Hamming distance between these strings.
    - **Hamming distance**: total num of mismatches between strings p and q 
        - Position i in k-mers p and q is a **mistmatch** if symbols at position i of 2 strings not equiv.
    - code is in bi_5_hammingDistance.py
___

## Approximate Pattern Matching Problem: Find all approximate occurences of a pattern in a string
- Input: Strings Pattern and Text along with an integer d.
- Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    - code is in bi_5_approxPatternMatch.py using the HammingDistance routine
___

## Now modify Frequent Words to find DnaA boxes
- by identifying frequent k-mers with mistmatches
- Given input strings Text and Pattern as well as an integer d, we extend the definition of PatternCount to the function ApproximatePatternCount(Pattern, Text, d)
    - code found in bi_5_approxPatternCount.py

## Final attempt
- With the modified algorithm we identify the most frequent 9-mers (with 1 mismatch) within a window of length 500 starting at position 3923620 of the E. coli genome.
    - The experimentally confirmed DnaA box in E. coli (TTATCCACA) is indeed a most frequent 9-mer, along with its reverse complement TGTGGATAA (with 1 mismatch)
    - However, we find 5 other 9-mers with their complements appearing 4 times with 1 mismatch