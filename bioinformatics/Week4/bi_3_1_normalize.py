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

def main():
    Probabilities = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
    print(Normalize(Probabilities))

if __name__ == '__main__':
    main()