def get_mean_median_mode(arr):
    n = len(arr)
    sum=0.0
    for i in range(n):
        sum += float(arr[i])
    mean = sum/n
    if n%2==0:
        median = (arr[(n/2)-1]+arr[(n/2)])*0.5
    else:
        median = arr[(n/2)]
    #print float(mean)
    #print arr
    #print float(median)
    x = [(i, arr.count(i)) for i in arr]
    x.sort(key=lambda x: x[1], reverse=True)
    #print x
    mode = x[0][0]
    return (mean, median, mode)    

def main():
    d = raw_input("Enter list \n").split(" ")
    d = [float(i) for i in d]
    d = sorted(d)
    m1, m2, m3 = get_mean_median_mode(d)
    print "List : ", d
    print "Mean : ", m1
    print "Median : ", m2
    print "Mode : ", m3


if __name__ == "__main__":
    main()