"""
Variables exercise

Q1 Identify the datatype for these values/ results of expressions:

4			integer
3.5			float
“hello”		string
True		boolean
3 + 4.5     float


Q2 
a = 2
b = 1.5
c = '12'
d = 'alan'

With reference to the codes above, write the result of the following commands:
If the command lead to error, state “error”
If the result is a string value, enclose in quotes

float(a)    	2.0
str(a)      	'2'
int(d)      	error
int(b)			1
float(c)		12.0
str(int(b)) 	'1'
"""

# Q3 Write the code to perform the following tasks:
# Create a variable X and assign it a value of 5.
x = 5

# Create a variable y and assign it a value of 1.5
y = 1.5

# Create a variable z and assign it a value of “hello world”
z = "hello world"

# Create a variable is_raining and assign it with a value of False. 
is_raining = False

# Create another variable is_weekday and assign it with a value of True.
is_weekday = True

# Concatenate (Join) two values “Happy” and “Birthday” with a space in between
# Assigned the result to a variable greeting.
greeting = "Happy" + " " + "Birthday"

# Convert the integer: 42 to a float.
float(42)

# Convert the string: “5” to an integer.
int("5")

# Convert the number: 5.6 to a string.
str(5.6)


"""
Q3.2 Examine each of the python command given. State the name of the variable that is being 
assigned a value, the value assigned and the data type of the variable. 
The answer for the first statement is given as example:

				    Variable / value / datatype
weight = 65.5		    weight / 65.5 / float
gpa = 3			        gpa / 3 / integer
gender = “Female”       gender / "Female" / string
Enabled = False		    Enabled / False / boolean
height = 180 + 5.0 	    height / 185.0 / float
w = float(4) + 3 	    w / 7.0 / float
x = 7/2   			    x / 3.5 / float
y = int(4.5) + 5.0		y / 9.0 / float
z = str(“1”) * 4 		z / 1111 / string
total = 42 + 2 		    total / 44 / integer
number = “42” + “2”	    numer / 422 / string
"""

# Q4.1 Write a program perform simple addition of two numbers
# Create the variables: x and y.  Assign x with the value 1 and y with the value 2. 
x = 1
y = 2

# Create the variable z and store the value of x + y in it.
z = x + y

# Q4.2 Write a program that compute the balance in a saving account after a withdrawal
# Assign variable saving with the value 150 and variable withdrawal with the value 99.  
saving = 150
withdrawal = 99

# Create the variable balance and store the value of saving – withdrawal in it. 
balance = saving - withdrawal

# Q4.3 Write a program that compute the area of a rectangle of length 10.5cm and breath 7.5cm:
# Assign variable length with the value of 10.5 and assign variable breadth with value of 7.5.  
length = 10.5
breadth = 7.5

# Calculate the area of a rectangle with the variables length and breadth, and store the result in the variable area. 
area = length * breadth

# Python exercises question(s)
# 1)	Write a program to ask the user to type in their Username and Password.
# Then display a welcome message for the user.
user = input("Enter your username: ")
password = input("Enter your password: ")

print("Welcome back " + user + "!")