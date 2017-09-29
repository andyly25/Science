from bi2_2_patternCount import PatternCount

# So here's our dictionary counter
def CountDict(text, k):
    # creating a blank dictionary
    count = {}
    # loop through length - k + 1 of text
    for i in range(len(text)-k+1):
        # grab a pattern
        pattern = text[i:i+k]
        # now we check it through the function we made prvious and count its occurence
        count[i] = PatternCount(pattern, text)
    return count

text = "CCGAACACCCGTACACCGAACACCACACCACACCTTGCACACCACACCTACACCACACACCACACCGGACACCCACACCCACACCACGAACACCGAGAGTACACCTA"
k = 5
# uncomment if you want to test
# print(CountDict(text, k))

# Now we can generate the most frequent kmers in text 
def frequentWords(text, k):
    # making an empty dictionary
    frequentPatterns = []
    # make a dictionary of all the key pair values
    count = CountDict(text, k)
    # now organize by the max
    m = max(count.values())
    # now we are going through each item in dictionary
    for i in count:
        # and if we see a match with max, we append to our frequent patterns
        if count[i] == m:
            frequentPatterns.append(text[i:i+k])
    # return 
    return frequentPatterns

k=5
text2 = "CCGAACACCCGTACACCGAACACCACACCACACCTTGCACACCACACCTACACCACACACCACACCGGACACCCACACCCACACCACGAACACCGAGAGTACACCTA"
print(frequentWords(text2, k))


# Here's the full code:
'''
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return FrequentPatterns

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(text, k):
    # creating a blank dictionary
    count = {}
    # loop through length - k + 1 of text
    for i in range(len(text)-k+1):
        # grab a pattern
        pattern = text[i:i+k]
        # now we check it through the function we made prvious and count its occurence
        count[i] = PatternCount(pattern, text)
    return count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    # your code here
    for i in range(len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count + 1
    return count
'''