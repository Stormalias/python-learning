import random
import time
import os

'''
Design and implement a main menu for an ATM system. The menu should present the available options and allow users to choose an option  

'''

'''
Data
This section contains all data production and variable assignment. These variables, lists, and dictionaries will be used
in the functions later on
'''

accountBal = [round(random.uniform(1,1000), 2) for i in range(10)] # Account balance values initialisation
accountID = random.sample(range(11111,55555), 10) # Account id values initialisation
last_transaction = [[accountBal[i], 'No Prior Transaction'] for i in range(10)] #updated every transaction, starts current balance

mainDict = dict(zip(accountID, accountBal)) # Dictionary matching account ID to account balances
transactDict = dict(zip(accountID, last_transaction)) # Dictionary matchin account ID to last_transaction values
''' End of Section '''

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
    print("\nBANK OF VISVANATH\nMoney: We Want Yours!")
    print("\nMain Menu")
    print("\n---------------")
    print("\n1) Balance Inquiry")
    print("2) Withdrawal")
    print("3) Deposit")
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


#option 1: Displays account numbers, and upon input of account number will display balance and last transaction
def option1():
    print("Account numbers")
    print(*accountID, sep='\n') # shows current accounts
    
    try: # exception handling
        reqAcc = int(input("Enter the account ID you wish to view: ")) # ensures account ID is integer
        print(f"The balance for {reqAcc} is ${mainDict.get(reqAcc)}") # ensures account ID is valid
    except:
        tryAgain = input("Invalid account ID.\nType any key return to main menu or T to try again: ")
        if tryAgain == 'T':
            option1() # offers option to try again
        else:
            exceptReturn() # or option to return to main menu

    
    prevTrans = transactDict.get(reqAcc) # list value assigned to account id, for previous transaction
    print(f"Last transaction: {prevTrans[1]}")
    print(f"Previous Balance: ${prevTrans[0]}")
    
    returner() # return to main menu dialog


#option 2: Displays account numbers, requesting account ID and withdrawal amount, then updating values as required
def option2():
    print("Account numbers")
    print(*accountID, sep='\n') # shows current accounts
    while True:
        try: # exception handling
            reqAcc = int(input("Enter the account ID: ")) # ensures account ID is integer
            amountWithdraw = float(input("Enter the amount you wish to withdraw: $ ")) # ensures withdrawal amount is float
            currentBal = mainDict.get(reqAcc) # ensures account ID is valid
            if amountWithdraw > currentBal: # ensures withdrawal is within limits
                print("Amount requested to withdraw is more than what is currently in account")
                print(f"Current balance is {currentBal}. Please try again")
                continue
            elif amountWithdraw < 0: # ensures withdrawal amount is a positive number
                raise TypeError
            else:
                break
        except:
            tryAgain = input("Invalid input.\nType any key return to main menu or T to try again: ")
            if tryAgain == 'T':
                continue # offers option to try again
            else:
                exceptReturn() # or option to return to main menu

    
    newBal = currentBal - amountWithdraw # calculates new balance after withdrawal
    print(f"You have withdrawn ${amountWithdraw} from {reqAcc}")
    print(f"Your new balance is ${newBal}") # prints for user

    transactDict.get(reqAcc)[0] = currentBal
    transactDict.get(reqAcc)[1] = 'Withdrawal' # replaces values for last transaction
    mainDict[reqAcc] = newBal # updates current balance in main dictionary
    
    returner() # return to main menu dialog


#option 3: Displays account numbers, requesting account ID and deposit amount, then updating values as required
def option3():
    print("Account numbers")
    print(*accountID, sep='\n') # shows current accounts
    while True:
        try: # exception handling
            reqAcc = int(input("Enter the account ID: ")) # ensures account ID is integer
            amountDeposit = float(input("Enter the amount you wish to deposit: $ ")) # ensures deposit amount is float
            currentBal = mainDict.get(reqAcc) # ensures account ID is valid
            if amountDeposit < 0: # ensures desposit amount is positive number
                raise TypeError
            else:
                break
        except:
            tryAgain = input("Invalid input.\nType any key return to main menu or T to try again: ")
            if tryAgain == 'T':
                continue # offers option to try again
            else:
                exceptReturn() # or option to return to main menu
    

    newBal = currentBal + amountDeposit # calculates new balance after deposit
    print(f"You have deposited ${amountDeposit} from {reqAcc}")
    print(f"Your new balance is ${newBal}") # prints to the user

    transactDict.get(reqAcc)[0] = currentBal
    transactDict.get(reqAcc)[1] = 'Deposit' # replaces values for last transaction
    mainDict[reqAcc] = newBal # updates current balance in main dictionary
    
    returner() # return to main menu dialog
''' End of Section'''


mainMenu() # Program Initialisation