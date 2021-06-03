def weightedMean(X, W):
    # Write your code here
    a = 0
    for i in range(len(X)):
        a += X[i] * W[i]
    print("{:.1f}".format(a / sum(W))) 