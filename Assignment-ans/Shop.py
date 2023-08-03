import time
import os
import random

'''
Q2 Design and implement a main menu for ordering system. the main menu should present the available options and allow users to choose an option.  

'''

'''
Data
This section contains all data production and variable assignment. These variables, lists, and dictionaries will be used
in the functions later on
'''

prodIDs = random.sample(range(1111,5555), 15)
inventory = [random.randrange(1,100) for i in range(15)]
prices = [round(random.uniform(1,100), 2) for i in range(15)]

# Manual product line naming list, as creating random words that make sense would need a library to be pip installed
products = ["Gaming Chair", "Gaming Mouse", "Corsair mousepad", "Wireless Headphones", "Lightsaber", "Airbus A380",\
            "Covid Vaccine", "Ballpoint Pen", "Classical Guitar", "Arsenal FC Jersey", "Bigfoot's Tooth", "Python", "Cat",\
            "T-Shirt", "Hairband"]


# ValueList creation. This list contains name, number in stock and prices. Will be used as value against product ID as key
valueList = []
i = 0
while i < len(prodIDs): 
    innerList = [products[i], inventory[i], prices[i]]
    valueList.append(innerList)
    i += 1

mainDict = dict(zip(prodIDs, valueList)) # Maps valueList per product to product ID
'''End of Section'''

'''
Functions
This section lists out the functions used within the program
'''
# Return to main menu function in a form of interactable dialog
def returner():
    x = input("Press enter to return to main menu\n")
    if x:
        mainMenu()
    else:
        mainMenu()


# Exception return to menu function in a form of 3 second count down
def exceptReturn():
    print("Returning to main menu in 3 seconds")
    time.sleep(1)
    print("Returning to main menu in 2 seconds")
    time.sleep(1)
    print("Returning to main menu in 1 seconds")
    time.sleep(1)

    os.system('cls')
    mainMenu()


# Main Menu        
def mainMenu():
    print("\nPRAVAL'S EVERYTHING STORE\nWhere the impossible becomes plausible")
    print("\nMain Menu")
    print("\n---------------")
    print("\n1) Product List")
    print("2) Product Availability")
    print("3) Order placement")
    print("4) Exit")

    try: # Menu selection
        selection = int(input("\nPlease enter an option (1-4): ")) # ensures selection is integer
        if selection < 1 or selection > 4: # ensures selection is valid
            raise TypeError
    except:
        print("Invalid selection")
        exceptReturn()
        
    # Functions assigned to option numbers
    if selection == 1: 
        option1()
    elif selection == 2:
        option2()
    elif selection == 3:
        option3()
    elif selection == 4:
        print("Goodbye!")
        time.sleep(1) # Flavour
        exit() # Stops the programn to prevent any un intended errors, and quits
    else:
        print("Something went wrong you. You shouldn't be here")
        exceptReturn() # if somehow the exception handler doesn't catch something


# option 1: Display list of product names, id and prices
def option1():
    displayList = [["#","PRODUCT", "PRODUCT ID", "PRICE"]] # Header row

    i = 0
    while i < len(prodIDs): # Adds each line of product, ID and price
        tmp = (i+1, products[i], prodIDs[i], f'${prices[i]}')
        displayList.append(tmp)
        i += 1

    for row in displayList: # Formats list in neat columns
        print("{: <3} {: <30} {: <20} {: <20}".format(*row))

    returner() # return to main menu dialog


# option 2: User enters product id, and number in stock is displayed
def option2():
    try: # Exception handling
        idRequested = int(input("Enter product ID: ")) # ensures input is integer
        inStockNum = mainDict.get(idRequested)[1] 
        inStockItem = mainDict.get(idRequested)[0] # ensures that product ID is valid
    except:
        tryAgain = input("Invalid product ID.\nType any key return to main menu or T to try again: ")
        if tryAgain == 'T':
            option2() # offers option to try again
        else:
            exceptReturn() # or option to return to main menu

    print(f"Current stock of {inStockItem}: {inStockNum}") # prints current stock

    returner() # dialog to return to main menu


# option 3: User enters product id, and amount of items. Returned value is total price and a confirmation upon additional input from user
def option3():
    try: # Exception handling 
        idOrder = int(input("Enter product ID: "))
        orderQuant = int(input("Enter quantity request: ")) # first two ensures that inputs are integers
        inStock = mainDict.get(idOrder)[1] # ensures that product ID is valid
        if orderQuant < 0: # ensures that order amount is positive
            raise TypeError
    except:
        tryAgain = input("Invalid inputs.\nType any letter to return to main menu or T to try again: ")
        if tryAgain == 'T':
            option3() # offers option to try again
        else:
            exceptReturn() # or option to return to main menu

  

    if orderQuant > inStock: # checks against what is in stock
        print("Sorry that order request is too large")
        print(f"That item only has {inStock} in stock. Please input the order again") # displays what current stock is before restarting option
        option3() 
    else:
        orderPrice = mainDict.get(idOrder)[2]
        orderItem = mainDict.get(idOrder)[0]
        amountDue = round((orderPrice * orderQuant), 2) # calculation for total price
        print(f"Your order for {orderQuant} of {orderItem} comes to a total of ${amountDue}")
        confirm = input("Please confirm the order by typing CONFIRM: ") # confirmation dialog
        if confirm == 'CONFIRM':
            print("Transaction successful! Order placed")
            newAmount = inStock - orderQuant
            mainDict.get(idOrder)[1] = newAmount # updates stock values appropriately

            returner()
        else:
            tryAgain = input("Confrimation invalid. Order cancelled.\nType any letter to return to main menu or T to try again: ")
            if tryAgain == 'T':
                option3() # provides option to try again
            else:
                exceptReturn() # or return to main menu

'''End of Section'''


mainMenu() #initialise program start