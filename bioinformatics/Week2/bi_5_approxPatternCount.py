from bi_5_hammingDistance import HammingDistance

# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    for i in range(len(Text) - len(Pattern) + 1):
        # Here we grab off the chunk len of Pattern to compare with
        sliced = Text[i:i+len(Pattern)]
        # Then we use our HammingDistance function to compare differences
        hamResults = HammingDistance(sliced, Pattern)
        # if the results less than or equal to d
        if  hamResults <= d:
            # we append results into the array
            count += 1 
    # We return the positions 
    return count

def main():
    Pattern = "GAGG"
    Text = "TTTAGAGCCTTCAGAGG"
    d = 2
    print(ApproximatePatternCount(Pattern, Text, d))


if __name__ == '__main__':
    main()