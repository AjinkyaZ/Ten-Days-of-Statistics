from math import sqrt

def error_function(z):
    e = 2.71828
    # Using Horner's method since hackerrank does not allow importing scipy.integrate.quad :(
    t = 1.0/(1.0 + 0.5*abs(z))
    expo = e**(-z*z - 1.26551223 + t * ( 1.00002368 + t * ( 0.37409196 + t * ( 0.09678418 + t * (-0.18628806 + t * ( 0.27886807 + t * (-1.13520398 + t * ( 1.48851587 + t * (-0.82215223 + t * ( 0.17087277))))))))))
    x = 1 - t*expo
    if (z >= 0):
        return  x
    else: 
        return -x
    
def cumulative_dist_normal(x, mu, sigma):
    """Given a value x and mean and standard deviation for a random variable following
    the Normal distribution, find probability of the variable being less than x
    """
    error_input = (x-mu)/(sigma*sqrt(2))
    return 0.5*(1 + error_function(error_input))

def main_1():
    #Hackerrank problem on normal distribution
    print "Problem Statement\nGiven time to assemble a car as a random variable X having normal distribution mean of A hrs,\nand standard devation of B hours, find probability that a car can be assembled\nwithin a given set of bounds."
    d = [float(i) for i in raw_input("Enter Mean and Std.Dev for X:\n").split(" ")]
    mean_x = d[0]
    sd_x = d[1]
    r = [float(i) for i in raw_input("Enter lower and upper bounds for probable number of hours to assemble a car:\n").split(" ")]
    lower_b = r[0]
    upper_b = r[1]
    print "Probability that a car can be assembled within the given time constraints is {0:.3f}".format(cumulative_dist_normal(upper_b, mean_x, sd_x)-cumulative_dist_normal(lower_b, mean_x, sd_x))


def main_2():
    #Another Hackerrank problem on normal distribution
    print "Problem Statement\nGiven mean and std.dev for Physics grades for a group of students,\nand the distinction and passing bounds, find percentage of students who score above the distinction threshold,\nthose who pass, and those who fail."
    (mean, sd) = [int(i) for i in raw_input("Enter Mean and Std.Dev for student grades:\n").split(" ")]
    l1 = int(raw_input("Enter distiniction threshold:\n"))
    l2 = int(raw_input("Enter passing threshold:\n"))
    print "Percentage of students who obtain distinction is {0:.2f}%".format((1-cumulative_dist_normal(l1, mean, sd))*100)
    print "Percentage of students who pass is {0:.2f}%".format((1-cumulative_dist_normal(l2, mean, sd))*100)
    print "Percentage of students who fail is {0:.2f}%".format((cumulative_dist_normal(l2, mean, sd))*100)


def main():
    main_1()
    print "\n\n***********************************\n\n"
    main_2()


if __name__ == "__main__":
    main()