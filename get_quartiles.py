def get_median(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    if n%2==0:
        median=(arr[(n/2)-1]+arr[n/2])*0.5
    else:
        median=(arr[n/2])
    return median


def get_quartiles(arr):
    n = len(arr)
    q2=get_median(arr)
    if n%2==0:
        d1=arr[:(n/2)]
        d2=arr[(n/2):]
        q1=get_median(d1)
        q3=get_median(d2)
    else:
        d1=arr[:(n/2)]
        d2=arr[(n/2)+1:]
        q1=get_median(d1)
        q3=get_median(d2)
    return (q1, q2, q3)


def main():
    d = raw_input("Enter list\n").split()
    d = [int(i) for i in d]
    d = sorted(d)
    quartiles = get_quartiles(d)
    print "List : ", d
    print "Q1 : ", quartiles[0]
    print "Q2 : ", quartiles[1]
    print "Q3 : ", quartiles[2]

if __name__ == "__main__":
    main()