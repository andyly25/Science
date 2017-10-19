def PrNew(Text, Profile):
    # sets to 1 since we are multiplying into it, if it was 0... well we get nowhere
    result = 1
    # loop through len of text
    for i in range(len(Text)):
        # we grab the letter to use to find specific elements
        letter = Text[i]
        # now as we loop through we just mutiply the letter and position we are currently in string
        result *= Profile[letter][i]
    # we get our results with a lot decimals if not 0
    return result

def profileMostProbableNew(Text, k, Profile):
    # Set the initial result to be the first k-mer we check in case all values are under 0
    finalResult = Text[0:k]
    # print(finalResult)
    # initialize our max value var
    maxValue = 0
    # we loop through len of text minus k
    for i in range(len(Text) - k + 1):
        # Here we grab a k-mer to test
        textChunk = Text[i:i+k]
        # We run that kmer through our Pr function
        result = PrNew(textChunk, Profile)
        # so if the results is greater
        if result > maxValue:
            # we take that as out best kmer and continue comparing for max
            maxValue = result
            finalResult = textChunk
    return finalResult

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    # insert your code here
    motifs = []
    k = len(Profile['A'])
    for dna in Dna:
        probKmer = profileMostProbableNew(dna, k, Profile)
        motifs.append(probKmer)
    return motifs





def main():
    ProfileTestCase0= { 
        'A': [0.8, 0.0, 0.0, 0.2 ],
        'C': [ 0.0, 0.6, 0.2, 0.0], 
        'G': [ 0.2 ,0.2 ,0.8, 0.0], 
        'T': [ 0.0, 0.2, 0.0, 0.8]
        }   
    DnaTC0=['TTACCTTAAC','GATGTCTGTC','ACGGCGTTAG','CCCTAACGAG','CGTCAGAGGT']
    print(Motifs(ProfileTestCase0, DnaTC0))

if __name__ == '__main__':
    main()