from mean_median_mode import get_mean_median_mode
from standard_deviation import get_sd

def get_pearson_coeff(x, y):
    mean_x = get_mean_median_mode(x)[0]
    sd_x = get_sd(x)
    mean_y = get_mean_median_mode(y)[0]
    sd_y = get_sd(y)
    sum_x_y = 0
    for i in range(len(x)):
        sum_x_y += (x[i]-mean_x)*(y[i]-mean_y)
    return sum_x_y/(len(x)*sd_x*sd_y*1.0)

def main_1():
    #Hackerrank problem on pearson coefficient
    print "Problem Statement"
    print "Given two lists (of the same length), find Pearson Correlation Coefficient of the two lists."
    a=[float(i) for i in raw_input("Enter elements in first list:\n").split(" ")]
    b=[float(i) for i in raw_input("Enter elements in second list:\n").split(" ")]
    if len(a)!=len(b):
        print "Lists must be of the same size!"
        return
    print "Pearson Correlation Coefficient for the two lists is {0:.3f}".format(get_pearson_coeff(a, b))

def main():
    main_1()


if __name__ == "__main__":
    main()