# Question 1:
# Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Solution

for i in range(2000,3201):
    if ((i%7==0)  and (i%5!=0)):
        print(i,end=",")
print("\n")
# Question 2:
# Write a program which can compute the factorial of a given numbers.

# Solution:

# Using Loops:

n=int(input("Enter Number for Factorial "))
fact=1
for i in range(1,n+1):
    fact = fact * i
print(fact)

# Without the usage Loops:

def factorial(n,fact):
    fact=n*fact
   # print(fact)
    if(n-1):
        return factorial(n-1,fact)
    return fact
print(factorial(n,1))

# Question 3:
# With a given integral number n, 
# write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). 
# and then the program should print the dictionary

#Solution:

print({x:x*x for x in range(1,int(input("Enter Number for dict "))+1)}) # Dict Comperhension
    