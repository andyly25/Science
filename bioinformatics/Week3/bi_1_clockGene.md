# The Circadian Clock
- **circadian clock**: internal timekeeper of animal, plants, and bacteria
    - can malfunction causing a genetic disease called **delayed sleep-phase syndrome (DSPS)**
    - Question: how do individ. cells in animals and plants know what time it is?
        - can we explain why heart attacks occurs more in morning and asthma attacks at night?
        - can we identify the gene that can cause DSPS?
    - Early 1970s, Ron Konopka and Seymour Benzer identified mutant flies with abnormal circadian patterns to single gene.
        - 20 years later to find the genes in mammals and some having names of timeless, clock, cycle
    - We'll first focus on plants, since vital for plants and their photosynthesis, flowering and etc

___

## Gene Expression
- **Central Dogma of Moelecular Biology**: DNA makes RNA makes protein
    - DNA corresponding to gene is **transcribed** into a strand of RNA composed of 4 **ribonucleotides**
        - adenine (A), cytosine (C), guanine (G), and uracil (U) (replaces thymine)
        - gets translated into amino acid sequence of protein
        - Transcription replaces all occurences of T in DNA with U 
            - **codons**: 3-mers that the RNA strand is partitioned into
            - then each codon -> one of 20 amino acids by genetic code
                - the whole sequence represented as **amino acid string**
                - each of the 64 RNA codons encodes its own amino acid
                    - exception: 3 **stop codon** which halts translation
- **Gene expression**: Variance in production of a gene's transcript
    - cells able to transcribe different genes into RNA at different rates
    - explains why brain and skin cell can have same DNA but behave differently
    - Table below describe translation of RNA 3 mer (codon) into one of 20 amino acids
    ![20 amino acid chart](http://bioinformaticsalgorithms.com/images/Antibiotics/genetic_code.png "from stepik.org 20 amino acid chart")

___

## Detour: Discovery of Codons and Split Genes
- 1961, Sydney Brenner and Francis Crick est. rule of "one codon, one amino acid" during protein translation
    - Observed deleting single nucleotide or 2 consec. nucleotides in a gene dramatically alters the protein
- 1964: Charles Yanofsky that a gene and protein it produces are **collinear**
    - 1st codon codes for 1st amino acid in protein and so on.
- 1977: believed protein encoded by long string contiguous nucleotide triplets until discovery of **split genes**
    - by Phillip Sharp and Richard Roberts necessitated computational problem of predicting locations of genes using genomic sequence
    - Sharp hyrbridized RNA encoding an adenovirus protein called **hexon** against 1 strand adenovirus DNA
        - if  contiguous, expected to see one to one hybridization of RNA bases with DNA bases
    - discovered during RNA-DNA hybrdization under electron microscope
        - saw 3 loop structures (shows not contiguous)
        - shows that the hexon mRNA built from 4 non-contiguous fragments of adenovirus genome
            - it's called **exons**, separated by 3 fragments called **introns**
            - What happens to the introns?
                -  RNA transcribed from split gene (**precursor mRNA or pre-mRNA**) 
                    - should be longer than RNA used as template for protein synth. (**messenger RNA or mRNA**)
                - **splicing** occurs, where some biological process removes the intron in pre-mRNA and add exons into single mRNA string.
                    - carried out by the *spliceosome* ... really creative name.
                - introns are still a mystery, viewed as either junk DNA or could possibly contain important regulatory elemnts.

___

## Regulatory proteins
- Every plant cell keeps track of day and night independently of other cells.
    - 3 plant genes: LCY, CCA1, TOC1 are clock's master timekeepers
        - NOTE: I'm lazy so I shall call them L, CC and T
        - **regulatory proteins** they encode controlled by external factors (sunlight and etc) in order to allow organisms to adjust gene expression
        - e.g. T promotes L and CC and can work vice versa, which results in **negative feedback loop**
            - In morning, sunlight activates L and CC, triggers repression of TOC1 transcription 
            - And as it becomes dark, the opposite happens in this continuous cycle
        - Able to control transcription of other genes because the regulatory proteins that they encode are **transcription factors**
            - AKA master regulatory proteins that turns genes on and off
            - regulate by binding to a specific short DNA interval called **regulatory motif**
                - AKA **transcription factor binding site** in the **upstream region**
                    - 600-1000 nucelotide long region preceding start of the gene. 
        - It would be simple if regulatory motifs were completely conserved, but they may vary at some positions
            - Now we need to develop algorithms for motif finding.