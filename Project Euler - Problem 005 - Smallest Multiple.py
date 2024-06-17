# Project Euler  -  Problem 5  -  Smallest Multiple
# Written by Brandon Edmondson, 04 April 2024
 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder. What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# Import time to track how long code takes
import time

# Start time
start = time.time()

# Set how high the range will be (20 for this problem)
N = 1000
# Set p = 1 for first multiple
p = 1

def PrimeTest(n):
    # True until proven False
    Test = True
    
    # Test if number is even and not 2
    if n%2 == 0 and n != 2:
        Test = False
    else:
        # Set i to first odd value not including 1
        i = 3
        # Loop until i is at least half of n
        while i < n/2:
            # Test if it can be divided evenly
            if n%i == 0:
                # When if statement True set Test to False and break loop
                Test = False
                break
            else:
                # Count by 2s to keep it odd
                i += 2
    # Return the results
    return Test

def SmallestPrimeFactor(n):
    if PrimeTest(n) == True:
        return n
    else:
        for i in range(n-1):
            if n%(i+2) == 0 and PrimeTest(i+2) == True:
                return (i+2)
                break
            

for i in range(N):
    # Check if the value is already a factor
    if p%(i+1) != 0:
        # Use the SmallestPrimeFactor function to set n to the lowest divible prime of the current value of i
        n = SmallestPrimeFactor(i+1)
        # Multiple our number by lowest prime factor of the value
        p = p*n

print(p)


# Set end time and print total time by subtracting the starting time from the ending time
end = time.time()
print("Code time =",(end - start),"seconds")
