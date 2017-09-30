# def PatternMatching(Pattern, Genome):
#     positions = []

#     # my code here
#     for i in range(len(Genome) + 1 - len(Pattern)):
#         if Genome[i:i+len(Pattern)] == Pattern:
#             positions.append(i)
#     return positions

# print(PatternMatching("AA", "AATCAAGGAA"))



# Full code:
# Copy your PatternMatching function below this line.
def PatternMatching(Pattern, Genome):
    positions = []

    # my code here
    for i in range(len(Genome) + 1 - len(Pattern)):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


# Forgot how to read files, but here it is
path = 'Vibrio_cholerae.txt'
choleraeFile = open(path, 'r')
v_cholerae = choleraeFile.read()
choleraeFile.close()

# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
Pattern = "CTTGATCAT"
Genome = v_cholerae
positions = PatternMatching(Pattern, Genome)

# print the positions variable
print(positions)