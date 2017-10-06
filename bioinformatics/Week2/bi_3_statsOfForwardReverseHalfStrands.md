# Peculiar Statistics of the Forward and Reverse Half-Strands (HS)
- shortcuts: Forward half strands (FHS), Reverse HS(RHS)
- recap: as replication fork expands
    - DNA polymerase synth DNA quick on reverse HS and delays on forward HS
- How can this help us locate ori?
    - reverse lives double stranded for most of its life and forward single stranded
        - problem: single stranded DNA has higher chance of mutation
            - if 1/4 nucleotides in single strand has ^ tendencies than other to mutates
                - best to obsever shortage of this nucleotide on forward HS
        - nucleotide counts for *Thermotoga petrophila* shown below
            - ![*Thermotoga petrophila*](http://bioinformaticsalgorithms.com/images/Replication/t_petrophila_nucleotide_counts.png "from stepik.org")
            - C more frequent on reverse HS by 11617 difference
            - G less frequent on reverse HS by -9973 difference
    - Why is there a discrepency in the nucelotides?
        - C has tendency to mutate into T through **deanimation**
            - rates rise 100 fold when single stranded
                - decrease in C in FHS cause mistmatched pairs T-G
                - mismatched can mutate into T-A pairs when bond repaired in next round replication
                    - decrease in G on RHS
        - with this knowledge, we can try slide a window of len(Genome)//2 down
            - hoping that the window with fewest occurence of C will ~correspond to FHS 
            - most occurence of C will be RHS
            - and if we know where the FHS and RHS is we found ori!

___            
## Analyzing a genome's half-strands
- so far we assumed genomes were linear, however this time we are going with circular
- We should account for the wrap around at the end of genomes.
    - define string ExtendedGenome as `Genome+Genome[0:n//2]`
        - AKA: copy first half of genome and paste at end of string
    - keep track of # occurence of C by using a **symbol array**
        - i<sup>th</sup> of symbol array is = to # occurence of symbol in window len(Genome)//2 at pos i of ExtendedGenome
        - example: The symbol array for Genome equal to "AAAAGGGG" and symbol equal to "A".
            - how to look at it by a commenter
            - Original genome: AAAAGGGG, Size: 8, Window size: 4, Symbol to count: A
            - Extended genome: AAAAGGGG + AAAA (first half of the original genome)
            - array[0]: Number of A's in [0-4]=AAAA -> 4
            - array[1]: Number of A's in [1-5]=AAAG -> 3
            - array[2]: Number of A's in [2-6]=AAGG -> 2
            - array[3]: Number of A's in [3-7]=AGGG -> 1
            - array[4]: Number of A's in [4-8]=GGGG -> 0
            - array[5]: Number of A's in [5-9]=GGGA -> 1
        - symbol array in code is called: bi_3_symbolArray.py
    - One of the exercise was made so that time limit will always be exceeded. 
        - SymbolArray() is way too slow. so we need to make a more efficient algorithm
            - for loop makes n = len(Genome) iterations
            - then compare symbol against n//2 symbols of ExtendedGenome
            - this requires n<<sup>2</sup>//2 comparisons to compute
            - and e. coli contains 4.5 million nucleotides so need execute over 10 trillion symbol comparisons
___

## Inefficient to more efficient algorithm
- first thing is to analyze our for loop which currently does:
    - When we slide window one symbol to the right, the # occurence of symbol in window does not change much
        - inefficient to regenerate the entire array from scratch.
- We can instead view the sliding of window as remove first symbol and adding new symbol at the end.
    - new version is `bi_3_fasterSymbolArray.py`
    - Here's the image of a graph on E. coli using this algorithm
    - ![e. coli plot for symbol = C](http://bioinformaticsalgorithms.com/images/Replication/e-coli_symbol_array_c.png "From stepik.org showing plot of e.coli for symbol = C")
        - Max value of the array occurs ~ pos 1,600,000 and min ~ pos 4,000,000
        - we can infer FHS begins ~ 4mil, and RHS at 1.6mil
        - Since ori occurs where RHS transitions for FHS therefore ori is located around pos 4mil


___ 
## DETOUR: BIG-O NOTATION
- algorithms are measured in terms of its worst case running time, so that we are guaranteed will never behave worse than our worst case scenario
- **Big-O notation** describes running time of algorithm
    - if alg. for sort array of n nums takes n<sup>2</sup> operations we say that it is O(n<sup>2</sup>)
        - it can be any variations 2n<sup>2</sup> and etc but it will still be O(n<sup>2</sup>)
            - only cares about the term that grows fastest with respect to size of input.
        - function f(n) is Big-O of function g(n), or O(g(n)), when f(n) ≤ c · g(n) for some constant c and sufficiently large n. 
