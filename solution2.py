# Write code for algorithm 2 below
#2. Write a function that prints the natural numbers from 1 to n.

#
	#your code here
#
#output: 1 2 3

def natural_numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    else:
        print(lowerNum)
        natural_numbers(lowerNum + 1, higherNum)

n=10
natural_numbers(1,n)
