# Write code for algorithm 3 below
#3. Write a function that returns the nth elements in the Fibonacci Sequence.

def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=2
for i in range(n):
    print(fibonacci(i))