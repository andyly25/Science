from bi_5_hammingDistance import HammingDistance

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    # Basing off my bi3_2_patternMatching.py, we want to loop through len of Text - pattern
    for i in range(len(Text) - len(Pattern) + 1):
        # Here we grab off the chunk len of Pattern to compare with
        sliced = Text[i:i+len(Pattern)]
        # Then we use our HammingDistance function to compare differences
        hamResults = HammingDistance(sliced, Pattern)
        # if the results less than or equal to d
        if  hamResults <= d:
            # we append results into the array
            positions.append(i) 
    # We return the positions 
    return positions

def main():
    Pattern = "ATTCTGGA"
    Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    d = 3
    print(ApproximatePatternMatching(Pattern, Text, d))


if __name__ == '__main__':
    main()