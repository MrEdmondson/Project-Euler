# Project Euler  -  Problem 10  -  Summation of Primes
# Written by Brandon Edmondson, 10 May 2024

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Import time to track how long code takes
import time

# Start time
start = time.time()

# Intial condition for prime array and sum
prime_array = [2]
sum = 0

# The number that the code will stop at
stopping_value = 2000000

def PrimeTest(n,prime_array):
    # True until proven False
    Test = True
    
    # Check whether our number is 1 or 2
    if n == 1:
        Test = False
    elif n == 2:
        Test = True

    # Checking for prime
    else:
        # Check whether our number is prime by dividing it by all previous prime numbers within prime_array
        for i in range(len(prime_array)):
            if n % prime_array[i] == 0:
                Test = False
                break
        # If number is prime append it to the prime_array
        if Test == True:
            prime_array.append(n)

    # Return the array with our prime numbers
    return prime_array

# Loop through our numbers starting at 1 and ending with the stopping value
for i in range(1,stopping_value+1):
    prime_array = PrimeTest(i, prime_array)

# Sum all the elements within our prime_array
for i in range(len(prime_array)):
    sum += prime_array[i]

print(sum)
# Ans = 142913828922
# Time = 748.5391104221344 seconds

"""
# Finding the 100,000th prime number test
for i in range(1,stopping_value+1):
    if len(prime_array) == 100000:
        print(prime_array[-1])
        break
    else:
        prime_array = PrimeTest(i, prime_array)
# Ans = 1299709
# Time = 441.14699053764343 seconds (previous code time for this was 1313 seconds in Problem 7 test)
"""

# Set end time and print total time by subtracting the starting time from the ending time   
end = time.time() 
print("Code time =",(end - start),"seconds")