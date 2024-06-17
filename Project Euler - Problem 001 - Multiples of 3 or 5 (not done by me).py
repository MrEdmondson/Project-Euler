# Project Euler  -  Question 1  -  Multiples of 3 & 5
# Written by Matthew Walker, 20 August 2017
 
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are
#  multiples of 3 or 5, we get 3, 5, 6 and 9.
#  The sum of these multiples is 23.  Find the sum of
#  all the multiples of 3 or 5 below 1000.  ANSWER = 2318.
 
sum = 0 #variable to hold sum
 
# Iterate i from 0 to 99
# If i is divisible by 3 or 5, add to sum
for i in range(1000):
    if (i%3 == 0 or i%5==0):
        sum += i
 
# Print answer
print('The sum is: ' + str(sum))
