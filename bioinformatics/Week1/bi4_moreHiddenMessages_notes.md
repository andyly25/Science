# Explosion of hidden messages
- So from previous note we saw something interesting, but we shouldn't jump to conclusion yet.
    - We should check the ori regions of other bacteria and see if it was not a fluke
    - here we test the ori region of Thermotoga petrophila
        - code in bi4_1_testingOtherOri.py
    - The results is ... *drumrolls* ... there was no occurence of that same pattern within this bacteria
        - thus, different bacteria may use different DnaA boxes as hidden messages to the DnaA protein
    - so moving on, we see that 6 9-mers are repeated 3 or more times
        - "CCTACCACC" (along with its reverse complement "GGTGGTAGG") appears 5 times in the origin
- The clump finding problem
    - instead of searching for clumps similar 9-mers patterns, since bacterias may contain different messages
        - we should try to find every k-mer that forms a clump in genome. 
        - since ori is usually of length 500, 
            - we slide of that length across genome to find where a k-mer appears most often in short succession
___

## Find patterns forming clumps in a string
- Input: A string Genome and integers k, L, t
    - note: k = k mer, L = length, t = appears this many time
- Output: All distinct k-mers forming (L, t) clumps in Genome
    - They did it for us and stated
    - > When we used this algorithm to look for clumps in the Escherichia coli (E. coli) genome, the workhorse of bacterial genomics, we found hundreds of different 9-mers forming (500, 3)-clumps in this genome.  It is absolutely unclear which of these 9-mers might represent a DnaA box in the bacterium’s ori region.
    - unseasoned researcher might give up, but the more seasoned will try learn more about details of replication in hopes provide new insights to find ori.

### Hidden rant
Let's move my rant to here so it's not as easy to find

I think it is a good idea for me to try to learn some other science related knowledge since there are many jobs that requires it. Who knows if it will count since it is all connections, degrees, and memorize these trivia probably Googled up that we won't ever use in the workforce these days...
It should be more of: *can you learn?*

Give me an assignment and a couple days and I'll learn what is needed to get it done. Simple as that. There are vast amount of easily accessible knowledge on the web and learning what's needed is easier than ever. Can't expect people to be walking encyclopedias off the bat. 

Not like throw a ball park question of: define how the Big Bang came to be and be sure to name all the big honchos in those theories as best as you can. Be as detailed as you can as we are checking off from our checklist. Then they mark your name off the list and decide to never give a phone call, and if they did it will be: "We like you, but sorry there are better fishes in the sea."

It somehow became a rant...


___
[Previous](https://github.com/birisora/Science/blob/master/bioinformatics/Week1/bi3_hiddenMessageMore_notes.md) <strong>-</strong> [Main Page](https://github.com/birisora/Science/tree/master/bioinformatics) <strong>-</strong> [Next](https://github.com/birisora/Science/tree/master/bioinformatics/Week2)