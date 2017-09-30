# Some hidden messages are more suprising than others
- A and T, C and G are complements
    - having one strand of DNA and a supply of free floating nucleotides 
    - Messelson and Stahl in 1958 confirmed this model (considered most beautiful experiment in Biology)
        - ![complementary strands run in opposite directions](http://bioinformaticsalgorithms.com/images/Replication/reverse_complement.png "complementary strands run in opposite directions, from stepik.org")
        - the beginning and end of DNA strands denoted 5' (five prime) and 3'.
            - each dna strand read in 5' -> 3' direction and complementary runs opposite
        - *DETOUR*: 1950's biologists debated 3 models of DNA replication
            - **semiconservative**: each parent strand acts as template for synthesis of daughter strand
                - result each daughter mol. contains one parent and newly synthesized
            - **conservative**: entire double stranded DNA mol. served as template for new daughter.
                - result one mol with 2 parent strands and another with 2 newly synthesized strands
            - **dispersive**: some mechanism breaks DNA backbone into pieces and splices intervals of synth. DNA
                - each daughter molecules is a patchwork of old and new double stranded DNA
            - ![3 models from 1950s](https://stepik.org/media/attachments/lessons/13/replication_models_one_round_1.png "3 models 1950's from stepik.org")
            - Knowing DNA struct. contains <sup>14</sup>N (not sure if this will add superscript) and is more abundant than <sup>15</sup>N, Messelson and Stahl gre E. coli in <sup>5</sup>N medium causing bacteria gain weight
                - once bacterial DNA saturated with <sup>15</sup>N, transfered bacteria to less dense <sup>14</sup>
                - This results in the newly synthesized DNA containing exclusively <<sup>14</sup>N, and the 3 hypothesis for DNA replication predicted differently. 
                    - conservative predict half E. coli DNA will have <<sup>15</sup>N and therefore be heavier.
                        - and other half only <<sup>14</sup>N and be lighter
                        - when try separated DNA according to weight by usage of centrifuge, all DNA had same density (conservative method can now be shot down)
                    - The other 2 models predicted all DNA after one round replication having same density
                        - dispersive model should contain 25% <sup>15</sup>N and 75% <sup>14</sup>N and all having same density.
                        - Semiconservative would divide into 2 different densities.
                        - ![2nd round replication](https://stepik.org/media/attachments/lessons/13/replication_models_2.png "2nd round replication, from stepik.org")
                            - **semiconservative won** out, and even after 3 rounds, a quarted DNA would have <sup>15</sup>N and remaining 75% is lighter only <sup>14</sup>N
        - *DETOUR*: Directionality of DNA strands
            - sugar componant of nucleotide has ring of 5 carbon atoms labeled 1,2,3,4,5 on figure
                - ![sugar](https://stepik.org/media/attachments/lessons/14/nucleotide_4.png "sugar molecule from stepik.org")
                - the 5' is joined onto the phosphate group and 3' to neighboring nucleotide. 
                    - this is why the two ends of necleotides are called 5' end and 3' end
                    - As a standard a DNA strand always read in the 5' -> 3' direction
___

## Find the reverse complement of a DNA string
- the reverse complement of DNA is string formed by taking complementary nucleotide of each and then reversing the resulting string.
- input: A DNA string pattern
- output: The reverse complement of pattern
    - bi3_1_reverseStrings.py containings the code for this example
- Looking at the 4 most repeated 9-mers:
    - "ATGATCAAG",   "CTTGATCAT",   "TCTTGATCA",   "CTCTTGATC"
    - "ATGATCAAG" and "CTTGATCAT" are reverse complements of each other, resulting in the following six occurrences of these strings.

## Find all occurences of a pattern in a string
- input: Strings Pattern and Genome
- Output: all starting positions in Genome where Pattern appears as a substring
    - code is: bi3_2_patternMatching.py
    - So "ATGATCAAG" appears total of 17 times (3 times in ori, 14 within whole genome)
    - and its complement appears the same number of times as well