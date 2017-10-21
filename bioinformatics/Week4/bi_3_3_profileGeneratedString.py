'''
    Assemble this code into a function ProfileGeneratedString(Text, profile, k) 
    that takes a string Text, a profile matrix profile , and an integer k as input.  
    It should then return a randomly generated k-mer from Text whose probabilities 
    are generated from profile, as described above.
'''

# first, import the random package
import random

# then, copy Pr, Normalize, and WeightedDie below this line
def Pr(Text, Profile):
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

# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    # make a empty dict to store what we want
    newDict = {}
    # grab sum of all values
    probSum = sum(Probabilities.values())
    # iterating through keys and values of Probabilities..
    # forgot to have the .items() at end and wondered why didnt work
    for k, v in Probabilities.items():
        # store new values with the values/sum
        newDict[k] = v/probSum
    # return our results
    return newDict

    # Here's a one line version
    # return {key : probabilities[key] / sum(probabilities.values()) for key in probabilities}

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


# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    # your code here
    # grab len text and making a blank dictionary
    n = len(Text)
    probabilities = {}
    # now range over all possible kmers in Text
    for i in range(0, n-k+1):
        # compute probability of each one and placing probability into a dictionary
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    # then normalize the probabilities
    probabilities = Normalize(probabilities)
    # and return result of rolling a weighted die
    return WeightedDie(probabilities)


def main():
    Text = "AAACCCAAACCC"
    Profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
    k = 2
    print(ProfileGeneratedString(Text, Profile, k))

if __name__ == '__main__':
    main()