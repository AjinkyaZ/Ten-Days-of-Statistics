from mean_median_mode import get_mean_median_mode

def get_ls_regression_coeffs(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    xsqr = [i*i for i in x]
    sum_xsqr = sum(xsqr)
    xy = [x[i]*y[i] for i in range(len(x))]
    sum_xy = sum(xy)
    mean_x = get_mean_median_mode(x)[0]
    mean_y = get_mean_median_mode(y)[0]
    b = (5*(sum_xy)-sum_x*sum_y)/(5*sum_xsqr-(sum_x)**2)
    a = mean_y-b*(mean_x)
    return (a, b)


def main():
    #Hackerrank problem on least square linear regression line
    print "Problem Statement"
    print "Given length of two lists and elements of each (pairwise),"
    print "calculate the regression coefficient and find corresponding value for a given input"
    x = []
    y = []
    n = int(raw_input("Enter number of elements in both lists (should be equal):\n"))
    print "Enter elements of both lists pairwise:"
    for i in range(n):
        d = raw_input().split(" ")
        x.append(float(d[0]))
        y.append(float(d[1]))
    a, b = get_ls_regression_coeffs(x,y)
    X = float(raw_input("Enter X for which Y has to be calculated:\n"))
    print "Corresponding value for {0:.2f} is {1:.3f}".format(X, a+b*X)


if __name__ == "__main__":
    main()
