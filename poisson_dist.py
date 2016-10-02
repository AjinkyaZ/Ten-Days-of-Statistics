def facto(n):
    if n<=1: 
        return 1
    f = n*facto(n-1)
    return f


def n_combination_r(n, r):
    numer = facto(n)
    denom = facto(r)*facto(n-r)
    return numer/denom

def poisson_dist(l, k):
    e = 2.71828
    return (((l)**k)*(e**-l))/(facto(k))

def main1():
    #Hackerrank problem on poisson distribtion
    print "Problem Statement:\nGiven mean of variable following the Poisson distribution,\nfind probability of it being equal to N."
    a = float(raw_input("Enter mean for variable :\n"))
    b = int(raw_input("Enter value to test for:\n"))
    print "Probability of the variable being equal to {0:d} is {1:.3f}".format(b,poisson_dist(a, b))


def main():
    main1()


if __name__ == "__main__":
    main()