def facto(n):
    if n<=1: 
        return 1
    f = n*facto(n-1)
    return f

def n_combination_r(n, r):
    numer = facto(n)
    denom = facto(r)*facto(n-r)
    return numer/denom

def pmf_negative_binomial_dist(x, n, p):
    return n_combination_r(n-1, x-1)*(p**x)*((1-p)**(n-x))

def geometric_dist(n, p):
    return ((1-p)**(n-1))*(p)


def main_1():
    #Hackerrank problem on geometric distribution"
    print "Problem Statement:\nGiven probability of producing a defective product,\nfind probability of finding the first defect during the Nth inspection\n"
    prob = float(raw_input("Enter probability of producing defective product :\n"))
    if prob>1:
        print "Error! Probability cannot exceed 1"
    n_inspec = int(raw_input("Enter Nth inspection on which first defect must be found :\n"))
    print "Probability of finding first defect on the {0:d}th inspection is : {1:0.3f}".format(n_inspec, geometric_dist(n_inspec, prob))

def main_2():
    #Another hackerrank problem on geometric distribution"
    print "Problem Statement:\nnGiven probability of producing a defective product,\nfind probability of finding the first defect during the first N inspections\n"
    prob = float(raw_input("Enter probability of producing defective product :\n"))
    if prob>1:
        print "Error! Probability cannot exceed 1"
    n_inspec = int(raw_input("Enter N for first N inspections on which first defect must be found :\n"))
    tprob = 0
    for i in range(1, n_inspec+1):
        tprob += ((1-prob)**(i-1))*(prob)
    print "Probability of finding the first defect in the first {0:d} inspections is : {1:0.3f}".format(n_inspec, tprob) 


def main():
    main_1()
    print "\n\n***********************************\n\n"
    main_2()


if __name__ == "__main__":
    main()
