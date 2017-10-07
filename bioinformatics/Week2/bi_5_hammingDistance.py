# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    count = 0
    # loop through length of p
    for i in range(len(p)):
        # if we find a mismtach increment count
        if p[i] != q[i]:
            count += 1
    # Return our results
    return count

def main():
    p = "GGGCCGTTGGT"
    q = "GGACCGTTGAC"
    print(HammingDistance(p, q))

if __name__ == '__main__':
    main()
