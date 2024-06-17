# Project Euler  -  Problem 9  -  Special Pythagorean Triplet
# Written by Brandon Edmondson, 06 May 2024

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

# Import time to track how long code takes
import time

import math

# Start time
start = time.time()

# Min values for a, b, and c
a_min = 1
# b_min = 2 -> good to know but not useful needed
# c_min = 500 -> good to know but not needed

# Max values for a, b, and c
a_max = 249
b_max = 499
c_max = 997

# Set our test value to False by default
Test = False

# Loop through all possible values for a, b, and c
for a in range(a_min,a_max):
    # Check if our conditions have been met
    if Test == True:
        # Subtrack the extra 1 added to 'a' after our conditions have been met then stop loop
        a -= 1
        break
    for b in range(a+1,b_max):
        # Check if our conditions have been met
        if Test == True:
            # Subtrack the extra 1 added to 'b' after our conditions have been met then stop loop
            b -= 1
            break
        for c in range(b+1,c_max):
            # Check if our conditions have been met
            if a+b+c==1000 and c==math.sqrt(a**2 + b**2):
                # Set Test to True since our conditions have been met and then stop loop
                Test = True
                break

# Print answers and results
print(f"a: {a}, b: {b}, c: {c}")
print(f"Product: abc = {a*b*c}")

# Set end time and print total time by subtracting the starting time from the ending time
end = time.time()
print("Code time =",(end - start),"seconds")
