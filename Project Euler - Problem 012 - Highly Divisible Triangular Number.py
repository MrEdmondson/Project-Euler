# Project Euler  -  Problem 12  -  Highly Divisible Triangular Number
# Written by Brandon Edmondson, 14 June 2024

'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th
triangle number would be 1+2+3+4+5+6+7=28. The first ten terms would be:
1,3,6,10,15,21,28,36,45,55,...
Let us list the factors of the first seven triangle numbers:

1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
'''

# Import time to track how long code takes
import time

# Start time
start = time.time()

def countFactors(number):
    count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count += 1
            if i != number // i:
                count += 1
    return count

tri_num = 0
i = 1
count = 0

while count < 501:
    tri_num += i
    count = countFactors(tri_num)
    i += 1

print(f'{tri_num} has {count} divisors')

# Set end time and print total time by subtracting the starting time from the ending time   
end = time.time() 
print("Code time =",(end - start),"seconds")
