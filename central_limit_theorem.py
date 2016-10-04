from math import sqrt
from normal_dist import cumulative_dist_normal



def main_1():
    #Hackerrank problems on central limit theorem
    print "Problem Statement"
    print "A certain number of boxes must be transported using an elevator."
    print "Given the maximum capacity of the elevator, number of boxes, average weight and std.dev for the boxes,"
    print "find the probability that all of the boxes will be transported in a single run."
    maxw = float(raw_input("Enter Maximum weight:\n"))
    n = int(raw_input("Enter number of boxes:\n"))
    mean = float(raw_input("Enter mean weight of boxes:\n"))
    sd = float(raw_input("Enter standard deviation for boxes:\n"))
    new_mu = n*mean
    new_sigma = sqrt(n)*sd
    avg_weight = cumulative_dist_normal(maxw, new_mu, new_sigma)
    print "Probability that all {0:d} boxes can be transported is {1:.4f}".format(n, avg_weight)


def main_2():
    #Hackerrank problems on central limit theorem
    print "Problem Statement"
    print "Given the number of tickets left for a certain sporting event, number of people waiting in line,"
    print "and the mean and std.dev for number of tickets bought by a person, find the probability that"
    print "every person will be able to purchase tickets."
    tickets_left = int(raw_input("Enter num. of tickets left:\n"))
    n = int(raw_input("Enter number of people:\n"))
    mean = float(raw_input("Enter mean for tickets bought by a person:\n"))
    sd = float(raw_input("Enter standard deviation:\n"))
    new_mu = n*mean
    new_sigma = sqrt(n)*sd
    avg_weight = cumulative_dist_normal(tickets_left, new_mu, new_sigma)
    print "Probability that all {0:d} people will be able to puchase tickets is {1:.4f}".format(n, avg_weight)

def main_3():
    #Hackerrank problems on central limit theorem
    print "Problem Statement"
    print "Given a sample size and mean, std.dev of a population, find interval that"
    print "covers x percent of the population (expressed as 0<x<1)."
    sample_size = int(raw_input("Enter sample size:\n"))
    mean = float(raw_input("Enter mean for sample:\n"))
    sd = float(raw_input("Enter standard deviation:\n"))
    dist_frac = float(raw_input("Enter fraction of population in interval (decimal):\n"))
    if dist_frac<0 or dist_frac>1:
        print "Error! Fraction of population must be between 0 and 1."
        return
    # z --> standard score = (x-mu)/sigma
    z = 1.96
    new_mu = sample_size*mean
    new_sigma = sqrt(sample_size)*sd
    # By z-test, we know that lower interval = mu-z(sigma) and upper = mu+z(sigma)
    a = (new_mu - z*new_sigma)/sample_size
    b = (new_mu + z*new_sigma)/sample_size
    print "The interval in which {0:.2f}% of the population lies is from {1:.2f} to {2:.2f}".format(dist_frac*100,a,b)


def main():
    main_1()
    print "\n\n***********************************\n\n"
    main_2()
    print "\n\n***********************************\n\n"
    main_3()


if __name__ == "__main__":
    main()