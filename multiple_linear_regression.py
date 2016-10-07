from sklearn import linear_model

def main():
    #Hackerrank problem on multiple linear regression
    print "Problem Statement"
    print "Given the value of Y for n sets of m features,"
    print "such that Y = a + b1*f1 + b2*f2 + ... +bm*fm,"
    print "find the value of Y given another m features."
    (m, n) = [int(i) for i in raw_input("Enter values of m and n:\n").split(" ")]
    farr = []
    y = []
    for i in range(n):
        features = [float(i) for i in raw_input("Enter features:\n").split(" ")]
        y.append(float(raw_input("Enter value of Y for given features:\n")))
        farr.append(features)
    lm = linear_model.LinearRegression()
    lm.fit(farr, y)
    a = lm.intercept_
    b = lm.coef_
    fsets = [float(i) for i in raw_input("Enter features in set:\n").split(" ")]
    if len(fsets)!=m:
        print "Error! number of features is not equal to m"
    b = [i for i in b]
    bf=0
    for j in range(m):
        bf += b[j]*fsets[j]
    print "Print value of Y for the given features is {0:.2f}".format(a+bf)

if __name__ == "__main__":
    main()