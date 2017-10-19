# rolling dice to find motifs
- We will be using **randomized algorithms** that flip coins and roll dice to search for motifs
    - 18th century Comte de Buufon proved that they were useful by randomly drop needles onto paralled strips of wood.
        - used the result to approximate the constant pi
- **Las Vegas algorithms** delivers solutions guaranteed to be exact, despite still being random
- **Monte Carlo algorithms** are not guaranteed to return exact solutions, but can quickly find approximate solutions
    - speed allows run many times then chose best approximation over thousands of runs

___

## Detour: Buffon's Needle
- 1733 wrote essay on Medieval French game: *Le jeu de franc carreau*
    - a game where a player flips a coin and it lands on a checkerboard
    - wins if coin lands completely within one of the squares on the board and loses otherwise.
    - ![game board square](http://bioinformaticsalgorithms.com/images/Motifs/winning_franc_carreau.png "from stepik.org square")
- 4 decades later prublished paper on similar game where drop needle onto floor covered by wooden panels of equal width
    - Known as Buffon's needle where player wins if needle falls entirely within one of panels
    - once we fix a position for center of needle, its collection of different orientations sweep out a circle.
    - ![needle radius](http://bioinformaticsalgorithms.com/images/Motifs/buffons_needle_panels.png "from stepik.org")
    - 1812, Laplace pointed out that Buffon's needle could be used to approximate pi.
        - Then.. the first Monte Carlo algorithm has been born!
___

## Random motif search
- a bit lazy but now we are going to start using random in the code so...
    - look for the code in my repository and read my comments.
- Random motif search has advantage of finding longer motifs
    - captures implanted motif better than greedy motif search
    - can be run on larger number of iterations to discover better and better motifs
    - > Implanting strings just help us evaluate the algorithms. We know what we have to find: the implanted string. If the consensus sequences matches well the implanted string, then the algorithm works well. Then, having trust to the algorithm, we apply it in real life Dna sequences. Then we can be confident that the result is a motif (k-mer) that has some significance, for e.g it is the binding site for a transcription factor!