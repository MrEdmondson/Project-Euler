# Project Euler  -  Problem 2  -  Even Fibonacci Numbers
# Written by Brandon Edmondson, 03 March 2024
 
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 
# and, the first terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

sum = 2 # variable to hold sum of even numbers starting with 2
array = [0]*2
array[0] = 1 # first element of array
array[1] = 2 # second element of array

# Loop until value exceeds 4 million
while (array[1]<4e6):
    new = array[0] + array[1]
    array[0] = array[1]
    array[1] = new

    #Is number even?
    if array[1]%2 == 0:
        sum += array[1]

print("Sum is:", sum)