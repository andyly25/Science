
# some profile probability function thing
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


def main():
    # Given profile is
    profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
    }

    # We want to compute this for our exercise
    print(Pr("TCGTGGATTTCC", profile))
    print(Pr("ACGGGGATTACC", profile))

if __name__ == '__main__':
    main()