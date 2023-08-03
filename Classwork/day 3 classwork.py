import random
from statistics import mean, mode, median

#Classwork day 3
# Lists and tuples
# 1)	Write a program to:
# •	store a list of first name, last name and favourite colour for everyone in the class using a nested tuple
classList = [("Aragorn", "Elessar", "Silver",), ("Gandalf", "Greyheim", "White",), ("Peregrin", "Took", "Green",), ("Meriadoc", "Brandybuck", "Red",), ("Samwise", "Gamgee", "Gold",)]

# •	display all the favourite colours
for tuple in classList:
    print(tuple[2])

# •	prompt for a name in the list to display the unpacked tuple (each value on separate line)
userName = input("Enter the first name: ")
for tuple in classList:
    if tuple[0] == userName:
        for _ in tuple:
            print(_)


# 3)	Changing an ingredient’s list:
# •	create a list of ingredients for a recipe
cakeRecp = ["flour", "butter", "sugar", "salt", "pepper", "chocolate", "vanilla"]
print(cakeRecp)
# •	you need to remove one ingredient that is not adequate
cakeRecp.remove("pepper")
print(cakeRecp)
# •	add a new ingredient to the list
cakeRecp.append("eggs")
print(cakeRecp)
# •	show the changes in the list after each operation


# 4)	Create the square2020 list, to hold the square of numbers 1 to 2020 (using - List Comprehension). Display the list.
square2020 = [(i ** 2) for i in range(1,2021)]

# 5)	Using the squares list created in 4):
# •	display the list
print(square2020)
# •	display the square of numbers 1 to 10
print(square2020[0:10])
# •	display the first and the last item in the list
print(square2020[0], square2020[-1])
# •	display the square of 5, 6 and 7
print(square2020[4:7])


# 6)	Generate a long list of random integers.
ranList = [random.randrange(-999,999) for i in range(500)]
print(ranList)
# •	find the biggest number in the list
print(max(ranList))
# •	use other aggregate functions to describe the list as well
print(min(ranList))
print(sum(ranList))
print(mode(ranList))
print(mean(ranList))
print(median(ranList))

# 8)	Using this Customerinfo:

Customerinfo = [ [100, "Jill", 1001, 2001], [109, "Jack", 1002, 2002], [119, "Frances", 1007, 2007], [110, "Matt", 1008, 2008] ]

# •	create another list of the customer’s names
customerNames = [i[1] for i in Customerinfo]
# •	display the list in descending order
print(sorted(customerNames, reverse=True))

# Sets and dicts
# 1)	Write a program to generate a dictionary that contains (i, i*i) for each integral number between 1 and n (both included). 
# •	a given integral number ‘n’ is a constant in the program
# •	use it to generate the dictionary
# •	print the dictionary
# Suppose the following input is supplied to the program: 8
# Then, the output should be:

# {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64}

userMax = int(input("Enter your max value as integer: "))

outputDict = {}
i = 0
while i < userMax:
    v = i + 1 # cleaner than writing i+1 for values required
    outputDict[v] = v * v
    i += 1

print(outputDict)


# 2)	Use the zip() function to join the supplied lists as a dictionary of exam results and then 
# 		find the key that has the maximum score.

# Supplied lists:
keys = ["Adam", "Betty", "Cathy", "Donald"]
results = [75,95,80,80]

examResults = dict(zip(keys, results))
print(max(examResults, key=examResults.get))

# Answer below is also for qn2 if there are two maximum values in results(i.e. slightly longer way)
'''
examResults = dict(zip(keys, results))
maxResult = max(examResults.values())
maxList = [] # In case two results are both tied for maximum

for i, j in examResults.items():
    print(i)
    if j == maxResult:
        maxList.append(i)


print(maxList)
'''