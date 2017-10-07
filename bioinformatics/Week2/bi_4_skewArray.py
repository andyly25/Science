# Input:  A String Genome
# Output: Skew(Genome)
def Skew(Genome):
    skew = {} #initializing the dictionary
    # your code here
    # skew = {0: 0}
    # Genome = ' ' + Genome
    skew[0] = 0
    # we already initialized 0 so we start at position 1
    for i in range(1, len(Genome)+1):
        # Here we check if first element is a G
        if Genome[i-1] == "G":
            # if it is we increment by 1
            skew[i] = skew[i-1]+1
        # if it was a C we decrement by 1
        elif Genome[i-1] == "C":
            skew[i] = skew[i-1]-1
            # otherwise we just set the skew to = previous
        else:
            skew[i] = skew[i-1]
    return skew

# def main():
#     print(Skew("CATGGGCATCGGCCATACGCC"))

# # Having this won't let main be run when imported
# if __name__ == '__main__':
#     main()