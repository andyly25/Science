import math

def EntropyScore(Profile):
    score = 0

    # Loop through the length of a profile
    for j in range(len(Profile["A"])):
        # we go through each symbols keys/values
        for symbol in Profile.keys():
            # if their value is above 0
            v = Profile[symbol][j]
            if v>0:
                # we applu the entropy formula
                score += math.log2(v)*v
    # then we return the result multipled by - since part of formula
    return -score

profile = {}
profile["A"] = [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0]
profile["C"] = [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6]
profile["G"] = [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
profile["T"] = [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]

print(EntropyScore(profile)) #Result: 9.916290005356972