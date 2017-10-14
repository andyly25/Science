from bi_4_exercistBreak import Pr


# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
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
        result = Pr(textChunk, Profile)
        # so if the results is greater
        if result > maxValue:
            # we take that as out best kmer and continue comparing for max
            maxValue = result
            finalResult = textChunk
    return finalResult



def main():
    Profile = { 
      'A': [0.2, 0.2, 0.3, 0.2, 0.3],
      'C': [0.4, 0.3, 0.1, 0.5, 0.1],
      'G': [0.3, 0.3, 0.5, 0.2, 0.4],
      'T': [0.1, 0.2, 0.1, 0.1, 0.2]
    }

    Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    k = 5
    print(ProfileMostProbablePattern(Text, k, Profile))

if __name__ == '__main__':
    main()