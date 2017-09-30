# Explosiong of hidden messages
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