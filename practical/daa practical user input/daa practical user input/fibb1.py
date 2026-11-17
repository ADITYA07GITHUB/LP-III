##non recursive fibonacci series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c
print("this is the end of the non recursive fibonacci series")
##time complexity of non recursive fibonacci series is O(n) and space complexity is O(1)


##recursive fibonacci series
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")
print("this is the end of the recursive fibonacci series")
##time complexity of recursive fibonacci series is O(2^n) and space complexity is O(n)



# Line-by-line explanation for the non-recursive Fibonacci series code:
# Line 1: Taking user input
# n = int(input("Enter number of terms: "))



# - input() takes input from the user.
# - int() converts the input into an integer.
# - n stores how many Fibonacci numbers to print.
# Example: n = 7 means print 7 Fibonacci numbers.
# Line 2–3: Initialize variables
# a = 0b = 1



# - a stores the current Fibonacci number.
# - b stores the next Fibonacci number.
# Initially, a = 0 and b = 1.
# Line 4: For loop
# for i in range(n):



# The loop executes n times.

# If n = 5, the loop runs for i = 0, 1, 2, 3, 4.
# Line 5: Print Fibonacci number
# print(a, end=" ")



# - Prints the current value of a.
# - end=" " prints numbers on the same line with spaces.
# Line 6: Calculate next Fibonacci number
# c = a + b



# Adds the two numbers to calculate the next Fibonacci number.

# Example:
# a = 0
# b = 1
# c = 0 + 1 = 1


# Line 7–8: Update variables
# a = bb = c



# This moves the values forward.

# Example:

# Before updating:
# a = 0
# b = 1
# c = 1


# After updating:
# a = 1
# b = 1


# Now the loop can calculate the next number.
# Line-by-line explanation for the recursive Fibonacci series code:
# Line 1: Function declaration
# def fibonacci(n):



# - def is used to define a function in Python.
# - fibonacci is the function name.
# - n is the parameter passed to the function.
# Example: fibonacci(5) means we are calling the function with n = 5.
# Line 2–3: Base condition
# if n <= 1:    return n



# This is the base condition of recursion.
# - If n = 0 → return 0.
# - If n = 1 → return 1.
# The base condition stops the recursive calls.
# Line 4: Recursive function call
# return fibonacci(n-1) + fibonacci(n-2)



# This is the most important line.

# It calls the same function twice with smaller values.

# For example, when n = 4:
# fibonacci(4)
# = fibonacci(3) + fibonacci(2)
# = 2 + 1
# = 3


# The function keeps calling itself until n becomes 0 or 1.
# Line 5: Taking user input
# n = int(input("Enter number of terms: "))



# - input() takes input from the user.
# - int() converts the input into an integer.
# - n stores the number of Fibonacci terms to print.
# Example: If the user enters 5, n = 5.
# Line 6–7: Printing Fibonacci series
# for i in range(n):    print(fibonacci(i), end=" ")



# Suppose n = 5.

# The loop executes five times.
# i	Function call	Output
# 0	fibonacci(0)	0
# 1	fibonacci(1)	1
# 2	fibonacci(2)	1
# 3	fibonacci(3)	2
# 4	fibonacci(4)	3

# Final output: 0 1 1 2 3

# Why end=" "?

# By default, Python prints each result on a new line. end=" " prints all numbers on the same line separated by spaces.