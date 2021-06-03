def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2] + arr[n//2 - 1]) / 2
        arr1 = arr[:n//2]
        arr2 = arr[n//2:]
    else:
        median = arr[n//2]
        arr1 = arr[:n//2]
        arr2 = arr[n//2 + 1:]
    
    l = len(arr1)
 
    if l % 2 == 0:
        q1 = (arr1[l//2] + arr1[l//2 - 1]) / 2
        q2 = (arr2[l//2] + arr2[l//2 - 1]) / 2
    else:
        q1 = arr1[l//2]
        q2 = arr2[l//2]
    res = list(map(int, [q1, median, q2]))
    return res
