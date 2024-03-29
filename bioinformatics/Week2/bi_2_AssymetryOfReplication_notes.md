# Assymetry of Replication
- Replication process is **asymmetric**
    - forward and reverse half-strands have different fates 
        - reverse half-strands: can copy nucleotides from ori to ter moving in (3 -> 5)
        - forward half-strands: cannot move in 5->3 direction, so DNA polymerase must replicate backwards towards ori
            - must wait for replication fork open a little (~2000 nucleotides) until new primer forms
            - Dna starts replicating small chunk DNA from primer and backward in direction of ori until both forwards are completed.
        - ![correct repliation figure](http://bioinformaticsalgorithms.com/images/Replication/okazaki.png "from stepik.org")
        - problem is that forward half-strands has occasional stopping and restarting which can create **Okazaki fragments**
            - complementary to intervals on forward half strand.
    - when replication fork reaches ter, nearly complete but with gaps from disconnected Okazaki fragments
    - ![almost complete](http://bioinformaticsalgorithms.com/images/Replication/asymmetric_replication_almost_complete.png (from stepik.org nearly complete))
        - **DNA ligase**, an enzyme, sews together the consecutive Okazaki fragments. 
            - results in 2 daughter chromosomes and does not wait until after all Okazaki fragments have been replicated to start sewing. 
            - ![ligase sewing](http://bioinformaticsalgorithms.com/images/Replication/asymmetric_replication_complete.png "from stepik.org replication complete")
    - reverse half strand (AKA **leading half-strand**) traverses strand nonstop. (continuous)
    - forward half strand (AKA **lagging half-strands**) since used as template by many DNA polymerase stopping and starting replication. (fragmented)
    - here's a comment's explanation:
        -  > Nucelotides are the building blocks of DNA they have a 3' end and a 5' end. DNA has two anti-parallel strands, meaning one strand is 3' to 5' and its complementary strand runs 5' to 3'. DNA polymerase can only read/move 3' to 5' along a DNA template. The new DNA daughter however is built starting from the 5' end of the daughter strand and grows in the 3' direction no matter the directionality of the parent DNA template (because biochemistry and physics).  So for the parent strand thats already in 3' to 5', synthesis proceeds faster because polymerase moves continuously, hence leading strand. For the complementary strand template starting from 5' to 3', polymerase still has to read it in 3' to 5' and build the new strand from 5' to 3'. So it has to wait for the DNA to unzip and then synthesizes small fragments during this process, hence lagging strand. 
        - Also a youtube link provided about DNA: [DNA replication in 3D](https://www.youtube.com/watch?v=TNKWgcFPHqw)