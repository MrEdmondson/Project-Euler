# Project Euler  -  Problem 7  -  10001st Prime
# Written by Brandon Edmondson, 12 April 2024
 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th
# prime is 13. What is the 10,001st prime?

# Import time to track how long code takes
import time

# Start time
start = time.time()

def PrimeTest(n):
    # True until proven False
    Test = True
    
    # Test if number is even
    if n%2 == 0 and n != 2 or n == 1:
        Test = False
    elif n == 2:
        Test = True
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

# Set condition for loop
PrimeFound = False

# Initial values
i = int(1)

# Starting count for prime number skipping 2
n = int(1)

# The prime number being sought after
N = 10001

while PrimeFound == False:
    # Test whether i is prime
    if PrimeTest(i) == True:
        # Count the number of primes that have been found
        n+=1
        # Test whether we've found the number we're searching for
        if n == N:
            # Set condition to break loop when prime number found
            PrimeFound = True
        else:
            # Increase our tester value by 2 to keep it odd
            i+=2
    else:
        # Increase our tester value by 2 to keep it odd
        i+=2

print(i,"is prime number",N)

# Set end time and print total time by subtracting the starting time from the ending time
end = time.time()
print("Code time =",(end - start),"seconds")

# It took 1313 seconds to find the 100000th prime
