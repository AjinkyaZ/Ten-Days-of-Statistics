def get_weighted_mean(nums, weights):
    n1 = len(nums)
    n2 = len(weights)
    if n1!=n2:
        print "List of numbers and weights are not of the same length!"
        return
    else:
        n=n1
    sumw=0
    sumwx=0
    for i in range(n):
        sumwx += nums[i]*weights[i]
        sumw += weights[i]
    weighted_mean = sumwx/sumw
    return weighted_mean

def main():
    x = raw_input().split(" ")
    x = [float(i) for i in x]
    w = raw_input().split(" ")
    w = [float(i) for i in w]
    w_mean = get_weighted_mean(x, w)
    print w_mean

if __name__ == "__main__":
    main()
