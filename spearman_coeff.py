from pearson_coeff import get_pearson_coeff


def get_rank(m):
    seen = {}
    c = 0
    rank = []
    msorted = sorted(m)
    for i in range(len(m)):
        elem = msorted[i]
        if elem not in seen:
            c += 1
            seen[elem] = c
        else:
            continue
    for i in m:
        rank.append(seen[i])
    return rank


def get_spearman_coeff(x, y, duplicates):
    rank_x = get_rank(x)
    rank_y = get_rank(y)
    if duplicates:
        return get_pearson_coeff(rank_x, rank_y)
    else:
        d = 0
        n = len(x)
        for i in range(n):
            d += ((rank_x[i]-rank_y[i])**2)
        return 1 - (6*d)/float(n**3-n)



def main():
    #Hackkerank problem on spearman coefficient
    print "Problem Statement"
    print "Given two lists of equal length, having zero or more repeating elements,"
    print "Find Spearman's Rank Correlation coefficient for the two lists."
    a=[float(i) for i in raw_input("Enter elements in first list:\n").split(" ")]
    b=[float(i) for i in raw_input("Enter elements in second list:\n").split(" ")]
    if len(a)!=len(b):
        print "Lists must be of the same size!"
        return
    dups = 0
    for i in a:
        if a.count(i)>1:
            dups=1
            break
    for j in b:
        if b.count(j)>1:
            dups=1
            break
    print "Spearman's Rank Correlation Coefficient for the given lists is {0:.3f}".format(get_spearman_coeff(a, b, dups))


if __name__ == "__main__":
    main()