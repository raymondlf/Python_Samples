# return the nth number in the fibonacci sequenc
import sys

def findNFib(n):
    if(n == 1):
        return 0
    elif (n == 2):
	return 1
    else:
	return findNFib(n - 1) + findNFib(n - 2)

if (len(sys.argv) != 2):
    print("Usage: python findNthFibonacci.py <N>");
else:
    print(findNFib(int(sys.argv[1])))
