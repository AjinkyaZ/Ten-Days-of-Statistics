from mean_median_mode import get_mean_median_mode

def get_sd(arr):
    n = len(arr)
    mean = get_mean_median_mode(arr)[0]
    sum_sd = 0
    for i in arr:
        sum_sd += (i - mean)**2
    sd = (sum_sd/n)**0.5
    return sd


def main():
    d = [int(i) for i in raw_input("Enter list\n").split(" ")]
    print "List :", d
    print "Standard Deviation :", get_sd(d)


if __name__ == "__main__":
    main()