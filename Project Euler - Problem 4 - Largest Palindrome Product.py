# Project Euler  -  Problem 4  -  Largest Palindrome Product
# Written by Brandon Edmondson, 28 March 2024
 
# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

# Import time to track how long code takes
import time

# Start time
start = time.time()

pal = 0

# Loop through the range of 3-digit numbers starting high
for i in range(900):
    for j in range(900):
        n = 999-i
        m = 999-j
        product = n*m

        # Make an array from the product of two 3-digit numbers
        array = [int(digit) for digit in str(product)]

        # Test if the first and last match up as well as the middle digits
        if array[0] == array[-1] and array[1] == array[-2] and array[2] == array[-3] and product > pal:
            # Save the largest palindrome and the two 3-digit numbers that produced it
            pal = product
            x = n
            y = m

print("The palindrome is",pal,"and it comes from the product of",x,"and",y)


end = time.time()
print("Code time =",(end - start),"seconds")