# A Journey of a Thousand Miles...
## *Genome Replication*: An important task carried out in the cell where:
- cell must first replicate its genome so each of two daughter cells can inherit own copy
- 1953 *James Watson* and *Francis Crick* completed their paper on DNA double helix.
    - comments below mentions: that those two relied on a lot data collected from other scientists
        - Notable is largely uncredited photo 51 from Rosalind Franklin
    - conjectured the two strands of parent DNA unwinds during replication
        - Each act as template for synthesis of new strand.
        - Begins with pair of complementary strands, ends with two pairs of complementary strands
        - ![naive view of DNA replication from stepik.org](http://bioinformaticsalgorithms.com/images/Replication/semiconservative_replication.png "naive view of DNA replication from stepik.org")
            - A : Nucleotides Adenine
            - T : Thymine
            - C : Cytosine
            - G : Guanine
            - A <=> T, C <=> G (Assuming my <=> means complements)
        - The image is of DNA replication on a simple level
___

## Where does replication begin? In a region called *replication origin* or *ori*
- **DNA polymerases** is the molecuar copy machines.
- Locating ori helps to understand how cells replicate but also various biomedical problems
    - Usage of **viral vectors**: able to penetrate cell walls and is a genetically engineered mini-genome
        - They carry artificial genes that are used in agricultures e.g. frost resistant tomatoes
- gene therapy is to intentionally infect a patient who lacks crucial gene with viral vector containing an artificial gene encoding a therapeutic protein.
    - once inside patient it replicates itself and produces molecules of that protein
    - to do so, we need to know where the ori is in the vector's genome 
        - and that the genetic manipulations do not affect it.
___

## Here's a problem: 
- Assume genome has a single ori and represented as a DNA string, or seq. of nucleotides from A,C,G,T 
- Input: A DNA string Genome
- output: location of ori in Genome
- Does this biological problem represent a clearly stated computational problem?
    - No, we don't have the characteristics for ori, nor do we know how the patterns of the nucleotides will affect the location of the ori in the Genome. (my thoughts)
    - Biologists would plan an experiment to locate the ori; e.g. deleting short segments from genome and eventually find a segment whose deletion stops replication
    - Computer scientists would not start unless given more information befor starting
        - why should biologists care what comp sci wants?
            1. Computational methods are faster than experimental approaches
            2. results of many experiments cannot be interpretted without computational analysis
            3. experimental approaches to ori prediction are time consuming and only done for a few species so far.
___
[Previous](https://github.com/birisora/Science/tree/master/bioinformatics/Week1) <strong>-</strong> [Main Page](https://github.com/birisora/Science/tree/master/bioinformatics) <strong>-</strong> [Next](https://github.com/birisora/Science/blob/master/bioinformatics/Week1/bi2_hiddenMessagesInRep_notes.md)