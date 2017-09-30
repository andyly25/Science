# Here we try to reverse a string/text
def reverseString(text):
    # now make an empty string to store result
    result = ""
    # if we don't start at 1, it will print the first letter at the start
    for i in range(1, len(text)+1):
        # -1 is used to go backwards of the array
        result = result + text[-i]
    return result

text = "Apples"
print(reverseString(text))


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    # well just realized python does not have switch
    # switch(Nucleotide):
    #     case Nucleotide == 'A':
    #         comp = 'T'
    #         break
    #     case Nucleotide == 'T':
    #         comp = 'A'
    #         break
    #     case Nucleotide == "G":
    #         comp = 'C'
    #         break
    #     case Nucleotide == "C":
    #         comp = 'G'
    #         break
    #     Default:
    #         comp = 'use CAPITALS'
    # return comp

    # Using dictionary as substitution
    switch = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
        }
    return switch.get(Nucleotide, "nothing")

print(complement("A"))

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    comp = ''
    for i in range(len(Pattern)):
        comp += complement(Pattern[i])

    revComp = reverseString(comp)
    return revComp

text = "AAAACCCGGT"
print(ReverseComplement(text))


# Another person's solution using list comprehension:
def ReverseComplement2(Pattern):
    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    ''' 
    My head doesn't wrap around list comprehension as much but here's my take on it
    looking at the inside first 
    [d[x] for x in Pattern] : as it goes through pattern, each x can be used in d[x] to find its complement
    if x was A, then d[A] = T and it goes through the pattern like so
    '' is an empty string and we are joining the contents of that above step
    the [::-1] reverses the order as it's joining
    the :: is pretty new to me, it means extended slices, so if you do ::3 then grab elements by 3's
    '''
    return ''.join([d[x] for x in Pattern][::-1])

print(ReverseComplement2(text))