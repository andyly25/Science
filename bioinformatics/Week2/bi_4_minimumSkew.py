from bi_4_skewArray import Skew

# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = [] # output variable
    # your code here
    # We use our skew function we made to make a dictionary of key value skew data
    skewDict = Skew(Genome)
    # we grab out min value to use to find all occurences of min
    minValue = min(skewDict.values())
    # # Just to see what out min value is
    # print(minValue)
    # now we go through a list comprehension that will put into an array all occurence of the min appearing
    minKey = [k for k in skewDict if skewDict[k] == minValue]
    positions = minKey

    # # Without list comprehension we can do
    # for i in skewDict.keys():
    #     if skewDict[i] == minValue:
    #         positions.append(i)
    
    return positions



def main():
    Genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    print(Skew(Genome))
    print(MinimumSkew(Genome))

if __name__ == '__main__':
    main();