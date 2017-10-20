# first, import the random package
import random
# from operator import itemgetter

# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    # your code here
    # grabbing sum to use
    totsum = 0
    # grabbing a random value between 0 and 1
    randVal = random.uniform(0, 1)
    # print("randval is " + str(randVal))
    # now we loop through the key and values
    for k, v in Probabilities.items():
        # continue updating the total sum with values
        totsum += v
        # if our random value is < totsum, then current k is our kmer
        if randVal < totsum:
            kmer = k
            break
    return kmer

# #   Another version, needs to import itemgetter
#     for k, v in sorted(Probabilities.items(), key=itemgetter(1)):
#         # print("totsum is: " + str(totsum) + " randval: " + str(randVal) + " v is: " + str(v))
#         if totsum <= randVal < v + totsum:
#             return k
#         # print("totsum is now " + str(totsum))
#         totsum += v

def main():
    Probabilities = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
    print(WeightedDie(Probabilities))

if __name__ == '__main__':
    main()