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

# So how do you find this hidden message without knowing what it looks like?
- Problem: Find a "hidden message" in replication origin
    - Input: a string of text
    - Output: a hidden message in Text
        - My opinion: no, information not specific enough.
        - fun example was given from "The Gold Bug" where found a pattern and assuming the pirates spoke english, the most appeared symbols would represent letters THE and solved from there.
        - Brain is tired... will continue tomorrow