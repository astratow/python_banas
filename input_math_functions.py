# It is extremely important to be able to except input from users and Python makes it easy. The
# input() function displays a message and then assigns the users input up until they hit return
# (issue a newline) to a variable. That input is always a string so be prepared to cast if needed.
# CODE
# Name = input(‘What is your name :’)
# print(‘Hello’, name)
# You can also except 2 or more values with one input() function. Here we will ask for and then
# add together 2 numbers. I’ll also subtract, multiply, divide and use modulus on the values.
# Modulus returns the remainder of a division.
# I’ll also cast the strings to integers. The split() function splits user input based on whitespace
# between values.
# CODE
# # Assign 2 values by splitting user input at the whitespace
num_1, num_2 = input('Enter 2 Numbers :').split()
# # Convert strings into regular numbers (integers)
num_1 = int(num_1)
num_2 = int(num_2)
# # Add the values entered and store in sum
sum_1 = num_1 + num_2
# # Subtract the values and store in diﬀerence
diﬀerence = num_1 - num_2
# # Multiply the values and store in product
product = num_1 * num_2
# # Divide the values and store in quotient
quotient = num_1 / num_2
# # Use modulus on the values to find the remainder
remainder = num_1 % num_2
# # format() loads the variable values in order into the {} placeholders
print("{} + {} = {}".format(num_1, num_2, sum_1))
print("{} - {} = {}".format(num_1, num_2, diﬀerence))
print("{} * {} = {}".format(num_1, num_2, product))
print("{} / {} = {}".format(num_1, num_2, quotient))
print("{} % {} = {}".format(num_1, num_2, remainder))
# The format() function matches up values found between the parentheses that follow the
# keyword format with the {} (Curly Brackets) that are in the string of the print statement.