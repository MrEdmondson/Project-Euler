# Project Euler  -  Problem 3  -  Largest Prime Factor
# Written by Brandon Edmondson, 03 March 2024
 
# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143

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

'''
def PrimeList(n):
    if l == 0:
        primes = set()
    else:
        primes[l] = n
'''

# Gives us a range but note I've reduced it a lot so it doesn't take too long
num = int(600851475143/10000)

# Loop through the range
for i in range(num):
    # Test whether i is a factor of number
    if 600851475143%(2*i+1) == 0:
        #Test whether 2*i+1 is prime number
        if PrimeTest(2*i+1) == True:
            print(2*i+1)

# Set end time and print total time by subtracting the starting time from the ending time
end = time.time()
print("Code time =",(end - start),"seconds")
