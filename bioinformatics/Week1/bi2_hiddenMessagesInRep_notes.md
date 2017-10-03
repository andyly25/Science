# Hidden Messages in the Replication Origin (part 1)
- Here we will focus on finding ori in bacterial genome, most consisting of a single circular chromosome
    - region of bacterial genome encoding ori is ~few hundred nucleotides length
    - goal begin with bacteria with ori already known, and determine what makes its region special
        - allows us to then design a computational approach for other bacteria
        - Beginning bacteria is Vibrio cholerae (causes cholera)
        - it's nucleotide sequence found below
            - > atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaac ctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgacca cggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgactt gtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggatt acgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttagga tagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaat tgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaag atcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtt tccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc
            - I then do an exercise called: bi2_1_oriLength.py for length 540
        - **DnaA**: mediates the initiation of replication.
            - it is a protein that binds to short segment within the ori (AKA **DnaA box**)

___

## So how do you find this hidden message without knowing what it looks like?
- Problem: Find a "hidden message" in replication origin
    - Input: a string of text
    - Output: a hidden message in Text
        - My opinion: no, information not specific enough.
        - fun example was given from "The Gold Bug" where found a pattern and assuming the pirates spoke english, the most appeared symbols would represent letters THE and solved from there.
- So we opperate under asumption that DNA is a langauge of its own and try to find frequent words/patterns.
    - certain nucleotide strings appear often in small regions of genome.
        - since certain proteins can only bind to DNA
        - "ACTAT" is frequent substring of "ACA**ACTAT**GCAT**ACTAT**CGGGA**ACTAT**CCT"
        - sample code in bi2_2_patternCount.py
        - A string can have multiple most frequent k-mers
___

## Find the most frequent k-mers in a string
- input: string of text and integer k
- output: all most frequent k-mers in Text
    - straightforward alg. is compute how many times each k-mer substring of Text appears in Text, then select k-mer occuring the most
        - By generating an array where count is the # of times that the i-th k-mer of Text appears in Text
        - the code for this is in bi2_3_dictionaries.py
    - From what we found out, the 9-mer "ATGATCAAG" appears three times in the ori region of Vibrio cholerae 
        - experiments have shown that bacterial DnaA boxes are usually 9 nucleotides long. 
        - there are a total of 4 total 9 mers that appeared 3 times, so one of those 4 could be it.

___
[Previous](https://github.com/birisora/Science/blob/master/bioinformatics/Week1/bi1_genomeReplication_notes.md) <strong>-</strong> [Main Page](https://github.com/birisora/Science/tree/master/bioinformatics) <strong>-</strong> [Next](https://github.com/birisora/Science/blob/master/bioinformatics/Week1/bi3_hiddenMessageMore_notes.md)