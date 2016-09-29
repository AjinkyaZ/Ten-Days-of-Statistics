from quartiles import get_quartiles


def main():
    n=int(raw_input("Enter number of unique items\n"))
    d = raw_input("Enter items\n").split()
    d = [int(i) for i in d]
    f = raw_input("Enter item frequencies\n").split()
    f = [int(i) for i in f]
    if len(d)!=len(f):
        print "Error! incompatible array lengths!"
    df = []
    for i in range(n):
        for j in range(f[i]):
            df.append(d[i])
    df = sorted(df)
    #print df
    n=len(df)
    q1, q2, q3 = get_quartiles(df)
    print "List :", df
    print "Interquartile Range :", float(q3-q1)



if __name__ == "__main__":
    main()