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

def main_1():
    #Hackerrank problem on poisson distribtion
    print "Problem Statement:\nGiven mean of variable following the Poisson distribution,\nfind probability of it being equal to N."
    a = float(raw_input("Enter mean for variable :\n"))
    b = int(raw_input("Enter value to test for:\n"))
    print "Probability of the variable being equal to {0:d} is {1:.3f}".format(b,poisson_dist(a, b))


def main_2():
    #Another Hackerrank problem on poisson distribution
    print "Problem Statement:\nNumber of repairs for two machines A and B is a poisson random var, with means of x and y respectively"
    print "Given x and y, find Expected daily cost to repair each machine, where\na) Cost for A = 160+40(X*X)\nb) Cost for B = 128+40(Y*Y)"
    means = [float(i) for i in raw_input("Enter means for A and B's number of repairs\n").split(" ")]
    mean_a = means[0]
    mean_b = means[1]
    print  "Since number of repairs for both A and B are poisson random variables,\nE[X] = mean, Var(X) = mean and E[X*X] = Var(X) + E[X]*E[X]"
    E_Xsq_a = mean_a + (mean_a)**2
    E_Xsq_b = mean_b + (mean_b)**2
    expected_cost_a = 160+40*E_Xsq_a
    expected_cost_b = 128+40*E_Xsq_b
    print "Expected daily cost of A is {0:.3f}".format(expected_cost_a)
    print "Expected daily cost of B is {0:.3f}".format(expected_cost_b)


def main():
    main_1()
    print "\n\n***********************************\n\n"
    main_2()


if __name__ == "__main__":
    main()