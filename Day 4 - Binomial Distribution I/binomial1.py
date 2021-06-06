# Enter your code here. Read input from STDIN. Print output to STDOUT

# Factorial function
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

# Cominations Function
def combinator(n, x):
    return (fact(n)/(fact(x) * fact(n-x)))

# PMF
def b(n, x, p):
    return combinator(n, x) * (p**x) * ((1-p)**(n-x))


# odds = 1.09 / 1
def sol(odds):
    res = [b(6,i,(odds/(1 + odds))) for i in range(3, 7)]
    print(round(sum(res), 3))

if __name__ == '__main__':
    
    boys , girls = list(map(float, input().split(" ")))
    odds = boys / girls
    sol(odds)
