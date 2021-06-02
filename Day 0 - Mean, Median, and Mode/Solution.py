# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

def mean(arr, N):
    if N >= 1:
        res = np.sum(arr) / N
    return res

    
def median(arr, N):
    if N >= 1:
        arr = np.sort(arr)
        if N % 2 == 0:
            res = (arr[N//2] + arr[N//2 - 1]) / 2
        else:
            res = arr[N//2]
    return res
    
def mode(arr, N):
    if N >= 1:
        arr = np.sort(arr)
        dic = {x:0 for x in arr}  
        for elem in arr:
            if elem in dic.keys():
                dic[elem] += 1
        maxIndx = np.argmax(list(dic.values()))
        res = arr[maxIndx]
    return res


size = int(input())
numbers = list(map(int, input().split()))

print("{:.1f}".format(mean(numbers, size)))
print("{:.1f}".format(median(numbers, size)))
print(mode(numbers, size))
    
