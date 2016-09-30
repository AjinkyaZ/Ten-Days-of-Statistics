def facto(n):
    if n<=1: 
        return 1
    f = n*facto(n-1)
    return f


def n_combination_r(n, r):
    numer = facto(n)
    denom = facto(r)*facto(n-r)
    return numer/denom


def pmf_binomial_dist(x, n, p):
    return n_combination_r(n, x)*(p**x)*((1-p)**(n-x))


def main_1():
    #Hackerrank problem on binomial distribution"
    print "Problem Statement:\nGiven probability of boys to girls from births in a certain country,\nfind probability of getting atleast x boys from n births\n"
    prob_boy = float(raw_input("Enter probability of a boy being born (<=1) :\n"))
    if prob_boy>1:
        print "Error! probability cannot exceed 1. Please try again"
        return
    prob_girl = 1-prob_boy
    n = int(raw_input("Number of trials (births):\n"))
    x = int(raw_input("Minimum (at least) number of boys:\n"))
    prob_of_at_least_x_boys = 0
    for i in range(x, n+1):
        prob_of_at_least_x_boys+=pmf_binomial_dist(i, n, prob_boy)
    print "Probability of at least", x, "boys being born in", n,"births is :", prob_of_at_least_x_boys

def main_2():
    #Another hackerrank problem on binomial distribution"
    print "Problem Statement:\nA certain manufacturer finds that x percent pistons on average are rejected due to defects.\nGiven the percentage x and the number of pistons n in batch, find the probability of \na) At most 2 pistons are rejected.\nb) At least 2 pistons are rejected.\n"
    p_reject = float(raw_input("Enter probability of rejection (<=1)) : \n"))
    if p_reject>1:
        print "Error! probability cannot exceed 1. Please try again"
        return
    num_pistons = int(raw_input("Enter number of pistons in batch : \n"))
    prob_at_most_2_rejects = 0
    for i in range(0, 3):
        prob_at_most_2_rejects += pmf_binomial_dist(i, num_pistons, p_reject)
    print "Probability of at most 2 rejects : {0:0.3f}".format(prob_at_most_2_rejects)
    prob_at_least_2_rejects = 0
    for i in range(2, num_pistons+1):
        prob_at_least_2_rejects += pmf_binomial_dist(i, num_pistons, p_reject)
    print "Probability of at least 2 rejects : {0:0.3f}".format(prob_at_least_2_rejects) 


def main():
    main_1()
    print "\n\n***********************************\n\n"
    main_2()


if __name__ == "__main__":
    main()