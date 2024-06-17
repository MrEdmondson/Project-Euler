# Project Euler  -  Problem 6  -  Sum Square Difference
# Written by Brandon Edmondson, 05 April 2024
 
# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025-385=2640
# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.

# Import time to track how long code takes
import time

# Start time
start = time.time()

# Number of terms
N = 100

# Sum of squares formula
S1 = int((N*(N+1)*(2*N+1))/6)

# Square of sum formula
S2 = int((N*(N+1)/2)**2)

# Print the differenvce between the sum of the squares and the square of the sum
print("The differenvce between the sum of the squares and the square of the sum for the first",N,"natural numbers is",S2 - S1)

# Set end time and print total time by subtracting the starting time from the ending time
end = time.time()
print("Code time =",(end - start),"seconds")
