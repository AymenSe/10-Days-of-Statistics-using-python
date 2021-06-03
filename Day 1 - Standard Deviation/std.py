def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    n = len(arr)
    mean = sum(arr) / n
    temp = 0
    for ele in arr:
        temp += (ele - mean)**2
    std = (temp / n)**(1/2)
    print("{:.1f}".format(std))
