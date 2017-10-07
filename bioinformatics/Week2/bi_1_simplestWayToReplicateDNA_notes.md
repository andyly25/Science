# replication process
- Two complementary strands runs in opposite directions around circular chromosome unravel starting at ori
- ![replication image](http://bioinformaticsalgorithms.com/images/Replication/naive_replication.png "from stepik.org replication image")
    - **replication forks** occur as the strands unwind and expand in both directions around chromosome
        - until strands separate at **replication terminus**
            - located opposite to the ori in chromosome
    - Copying process occurs while strands are unraveling
        - **primer** is needed for DNA polymerase to begin replication.
            - short complementary segment that binds to the parent strand and jump start DNA polymerase
        - begins adding nucleotides beginning with primer and going around chromosome from ori to ter cw or ccw
            - when all reaches ter, DNA would have been completely replicated with two 2 pairs comp. strands
    - Problem: this current description assumes DNA polymerases can copy DNA in either direction along strand of DNA
        - Sadly, DNA polymerases are **unidirectional**, can only traverse a template strand in 3' -> 5' direction
        - There are 4 different half-strands of parent DNA connecting ori to ter.
            - two of these are traversed from ori to ter 5' -> 3' and called **forward half-strands**
            - the other half are **reverse half-strands** going in the 3' -> 5' directions
            - ![forward and reverse half-strands](http://bioinformaticsalgorithms.com/images/Replication/half_strands.png "from stepik.org")
            - So the ori will be found at the minimum

___

## Minimum skew problem
- Minimum Skew Problem:  Find a position in a genome where the skew diagram attains a minimum. 
    - Input: A DNA string Genome. 
    - Output: All integer(s) i minimizing Skew[i] among all values of i (from 0 to len(Genome)).
    - > Write a function MinSkew taking a DNA string Genome as input and returning all integers i minimizing Skew[i] for Genome. Then add this function to Replication.py. (Hint: make sure to call Skew(Genome) as a subroutine, and keep in mind that Python has a built-in min function in addition to max.)
        - code located at: bi_4_minimumSkew.py
        