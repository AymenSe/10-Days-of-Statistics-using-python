def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    n = sum(freqs)
    arr = []
    for i in range(len(freqs)):
        for j in range(freqs[i]):
            arr.append(values[i])
    
    arr = sorted(arr)
    
    if n % 2 == 0:
        left = arr[:n//2]
        right = arr[n//2:]
    else:
        left = arr[:n//2]
        right = arr[n//2 + 1:]
    
    n1 = len(left)
    
    if n1 % 2 == 0:
        q1 = (left[n1//2] + left[n1//2 - 1]) / 2
        q3 = (right[n1//2] + right[n1//2 - 1]) / 2
    else:
        q1 = left[n1//2]
        q3 = right[n1//2]

    intq = abs(q3 - q1)
    print("{:.1f}".format(intq))