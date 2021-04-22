#Global variable creation for everything to draw from.

#The list that will store all the users as class instances
listOfUsers = []
#The list that stores all valid colors for password recovery
listOfColors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "white", "black"]

class UserAccount:
    #Construct the user's account - all accounts start with a balance of 0
    def __init__(self, username = "", password = "", SecurityColor = ""):
        self.username = username
        self.password = password
        self.SecurityColor = SecurityColor
        self.accountBalance = 0

    def depositAmount(self):
        #While this function is running, continuously prompt the user to enter in a valid value.
        #The input should be able to be converted into a positive 2-point decimal number that is non-negative, or 0 if they want to return to the main menu
        #If a number such as -10 or 10.001 was given, you should inform the user that the number doesn't fit the format

        #EXAMPLES
        #Input: 0 Output: This is acceptable - it would return to the main menu by adding 0 to the accountBalance
        #Input: 10 Output: accountBalance is increased by 10
        #Input: 10.00 Output: accountBalance is increased by 10
        #Input: .01 Output: accountBalance is increased by .01
        #Input: -10 Output: "The number you gave does not follow the specified format. Please type in the number using the given format." and prompt the user again
        #Input djodgjpa Output:"Invalid input. Please make sure you entered a valid number." and prompt the user again
        while True:
            try:
                amountToDeposit = float(input("Enter the amount you wish to deposit. The accepted format is any positive number with non-zeros up to 2 decimal places (e.g. 10.99000). Enter 0 to return to the main menu: "))

                #The below checks that the number they give can be converted into a valid 2-point decimal number and that it's non-negative
                if (round(amountToDeposit,2) == amountToDeposit) and (amountToDeposit >= 0):
                    self.accountBalance += amountToDeposit
                    return
                #If the number fails this format, print such a message and tell them to choose again
                else:
                    print("The number you gave does not follow the specified format. Please type in the number using the given format.")
            #This exception message should only be generated if the input could not be converted into a float
            except ValueError:
                print("Invalid input. Please make sure you entered a valid number.")

    def withdrawAmount(self):
        #While this function is running, continuously prompt the user to enter in a valid value.
        #The input should be able to be converted into a positive 2-point decimal number that is non-negative, or 0 if they want to return to the main menu
        #If a number such as -10 or 10.001 was given, you should inform the user that the number doesn't fit the format
        #The function should also check after user input that the user has enough money in their accountBalance i.e. [self.accountBalance - amountToWithdraw < 0]
        #If they lack the money to make the withdraw, ask them to enter a smaller amount

        #EXAMPLES
        #Input: 0 Output: This is acceptable - it would return to the main menu by adding 0 to the accountBalance
        #Input: 10 Output: accountBalance is decreased by 10
        #Input: 10.00 Output: accountBalance is decreased by 10
        #Input: .01 Output: accountBalance is decreased by .01
        #Input: -10 Output: "The number you gave does not follow the specified format. Please type in the number using the given format." and prompt the user again
        #Input djodgjpa Output:"Invalid input. Please make sure you entered a valid number." and prompt the user again
        while True:
            try:
                amountToWithdraw = float(input("Enter the amount you wish to deposit. The accepted format is any positive number with non-zeros up to 2 decimal places (e.g. 10.99000). Enter 0 to return to the main menu: "))

                #The below checks that the number they give can be converted into a valid 2-point decimal number and that it's non-negative
                if (round(amountToWithdraw,2) == amountToWithdraw) and (amountToWithdraw >= 0):
                    if self.accountBalance - amountToWithdraw < 0:
                        print("You don't have enough in your account to withdraw that amount. Please enter a smaller amount.")
                    else:
                        self.accountBalance -= amountToWithdraw
                        return
                else:
                    print("The number you gave does not follow the specified format. Please type in the number using the given format.")
            except ValueError:
                print("Invalid input. Please make sure you entered a valid number.")

    def passwordRecovery(self):
        #While this function is running, the user gets 3 attempts to recover their password
        #The user should be reminded what the list of valid colors are
        #The user will need to have their input converted to lowercase as case should not matter - "Pink" should be considered "pink"
        #Each time they input a wrong answer, inform them that they have 1 less attempt i.e. "Wrong color. You have 2 attempts left."
        #If all 3 attempts are used and no correct color was given, inform the user and terminate the process.

        print("Beginning password recovery process.")

        #Give the user 3 attempts to input the color they chose during account creation. Also print out the valid list of colors.
        print("Please enter the security color you chose during account creation. You have 3 attempts. The valid list of colors was:",listOfColors)

        #Cycle through 3 attempts.
        for x in range(1, 4):
            userInput = input("You entered: ")
            userInput = userInput.lower()

            #If the user gives the correct color, print their password and terminate password recovery
            if userInput == self.SecurityColor:
                print("Your password is:",self.password)
                return
            
            #Otherwise, inform them that they have 1 less attempt i.e. "Wrong color. You have 2 attempts left."
            else:
                print("Wrong color. You have " + str((3-x)) + " attempts left.")

            #If all 3 attempts are used and no correct color was given, inform the user and terminate the process.
            if x == 3 and (userInput != self.SecurityColor):
                print("All attempts have been used. Terminating password recovery.")

    #This function serves as the main menu after successful login and will call upon all other functions that modify the user's account
    def mainMenu(self):
        while True:
            print("\nWelcome " + self.username + ". (Enter a number from the options below)")
            print("\tYour current balance is: $" + str(round(self.accountBalance,2)))
            print("\t1. Make a deposit")
            print("\t2. Make a withdrawal")
            print("\t3. Exit")

            userInput = input("You entered: ")
            while True:
                if userInput == "1":
                    print("Beginning deposit process.")
                    self.depositAmount()
                    break
                elif userInput == "2":
                    print("Beginning withdraw process.")
                    self.withdrawAmount()
                    break
                elif userInput == "3":
                    print("Logging user out.")
                    return
                else:
                    print("Invalid input. Reprinting main menu.")
                    break

def newAccountCreation():
    #USERNAME CREATION
    #Ask the user to choose a username and tell them that it's case sensitive - read below for why. Usernames like 123 or Bob123 or Bob 123 or !%# are fine.
    #Check if an account with that exact username already exists
    #If an exact match is found(e.g. We can't have two "Billy Bob" but we will accept a "Billy Bob" and a "Billy bob"), tell the user and make them pick a different one
    #If an exact match is found, you also need to check the entire list again incase the new username they chose is one that was scanned earlier in the list   

    global listOfUsers

    #Choose a username
    newUsername = input("Create a username for your account (case sensitive): ")
    
    #Check if an account with that exact username already exists
    x = 0
    while x < len(listOfUsers):
        if (newUsername == listOfUsers[x].username) :
            newUsername = input("This username is already taken. Please enter a different one: ")
            x = 0
        else:
            x += 1
    
    #PASSWORD CREATION
    #Ask the user to choose a password.
    #The password should be longer than 3 characters. If what they entered isn't, tell them why and make them enter a new password.
    #Ask the user to verify their password. If they enter in something different, tell them it doesn't match and make them enter it again.
    #If they instead enter 0 during verification, return them to making a new password.
    #Initialize newPassword and temporaryPassword for the purposes of stopping the user until they create a memorable password
    #It's rather primitive but I don't have a better solution currently
    newPassword = ""
    temporaryPassword = " "
    
    #Choose a password longer than 3 characters. We have this outer temporary != new repeated twice incase the user wants to start from scratch again
    while temporaryPassword != newPassword:
        newPassword = input("Create a password for your account that is longer than 3 characters: ")
        while len(newPassword) < 4:
            print("Your password does not meet the length requirement. Please try a longer password. ")
            newPassword = input("Create a password for your account that is longer than 3 characters: ")

        #Verify that the user remembers the password they just put or have them create a new password by entering 0
        while temporaryPassword != newPassword:
            temporaryPassword = input("Please verify your password by entering it again or type 0 to enter a new password: ")
            if (temporaryPassword == "0"):
                break
            elif (temporaryPassword != newPassword):
                print("The password your entered does not match the one made earlier.")

    #COLOR SELECTION FOR PASSWORD RECOVERY
    #Ask the user to choose a color from listOfColors
    #We should check that they chose a valid color
    #The user will need to have their input converted to lowercase as case should not matter - "Pink" should be considered "pink"
    #Ask the user to verify the color they chose. If they enter in something different, tell them it doesn't match and make them enter it again.
    #If they instead enter 0 during verification, let them choose a new color
    newSecurityColor = ""
    temporarySecurityColor = " "

    #Choose a valid color. We have this outer temporary != new repeated twice incase the user wants to start from scratch again
    while temporarySecurityColor != newSecurityColor:
        #Prompt user for their security color for password recovery
        print("Choose a color from the following list for later password recovery:", listOfColors)
        newSecurityColor = input("You entered: ")
        newSecurityColor = newSecurityColor.lower()
        #If the color they chose was not in the list, then prompt them to choose again until they do
        while not newSecurityColor in listOfColors:
            print("Invalid color chosen. Please select again from the following list:", listOfColors)
            newSecurityColor = input("You entered: ")
            newSecurityColor = newSecurityColor.lower()

        #Verify that the user remembers the color they just put or have them choose a new color by entering 0
        while temporarySecurityColor != newSecurityColor:
            temporarySecurityColor = (input("To verify that you have memorized your choice, please enter your security color again or type 0 to choose a new color: "))
            temporarySecurityColor = temporarySecurityColor.lower()

            if (temporarySecurityColor == "0"):
                break
            elif (temporarySecurityColor != newSecurityColor):
                print("The color your entered does not match the one chose earlier.")

    #After this is all complete, show the user their username, password, and chosen color one time and then initialize it as an anonymous object inside of listOfUsers
    print("Congratulatations! Your username is " + newUsername + ", your password is " + newPassword + ", and your security color is " + newSecurityColor + ".")
    listOfUsers.append(UserAccount(newUsername,newPassword, newSecurityColor))

def loginProcess():
    global listOfUsers

    #USERNAME MATCHING
    #If listOfUsers is empty, there's no point in trying to login. If this function is called and the list is empty, tell the user and terminate the process.
    #Otherwise, search through each listOfUsers element for a class instance with a matching username datafield.
    #If a match is found, proceed to #PASSWORD MATCHING
    #Otherwise, if the end of the list is reached and no match was found, tell the user the entered username was not found and terminate the process.
    #If listOfUsers is empty, there's no point in trying to login.

    #PASSWORD MATCHING
    #Once a username is successfully matched to a class object, prompt the user for their password
    #If what they entered doesn't match, tell them to enter it again or 0 to return to the main menu
    #If their input is correct, then call the mainMenu() function of their class instance

    if len(listOfUsers) == 0:
        print("The database is empty. Please create an account first.")

    else:
        #Prompt user for username
        attemptedLoginUsername = input("Please enter your username (case sensitive): ")

        #Scan through listOfUsers to find an object with a matching username data field
        for x in listOfUsers:
            #If found, prompt user for their password
            if x.username == attemptedLoginUsername:
                print(attemptedLoginUsername + " found in database.")
                attemptedLoginPassword = input("Please enter your password: ")

                #If the password is incorrect, continuously prompt for correct password or enter 0 to quit the login process using return
                while x.password != attemptedLoginPassword:
                    attemptedLoginPassword = input("Password is incorrect. Please try again or enter 0 to return to the main menu: ")
                    if (attemptedLoginPassword == "0"):
                        return
                    #Otherwise, the user will be pushed to the main menu for their account
                x.mainMenu()
                #This return terminates searching through the list for the user
                return

            #If the end of the list was reached and there was no match, print the appropriate message
            elif x == listOfUsers[-1] and x.username != attemptedLoginUsername:
                print(attemptedLoginUsername + " not found. Terminating process.")

def mainPasswordRecovery():
    #PASSWORD RECOVERY
    #If listOfUsers is empty, there's no point in trying to recover passwords. If this function is called and the list is empty, tell the user and terminate the process.
    #Otherwise, search through each listOfUsers element for a class instance with a matching username datafield.
    #If a match is found, then call the passwordRecovery() function of their class instance
    #Otherwise, if the end of the list is reached and no match was found, tell the user the entered username was not found and terminate the process.
    global listOfUsers

    #If the database is empty, there's no point in trying to do a password recovery.
    if len(listOfUsers) == 0:
        print("The database is empty. Please create an account first.")

    else:
        #Prompt user for username
        attemptedLoginUsername = input("Please enter your username (case sensitive): ")

        #Scan through listOfUsers to find an object with a matching username data field
        for x in listOfUsers:
            #If found, begin password recovery
            if x.username == attemptedLoginUsername:
                x.passwordRecovery()
                break

            #If the end of the list was reached and there was no match, print the appropriate message
            elif x == listOfUsers[-1] and x.username != attemptedLoginUsername:
                print(attemptedLoginUsername + " not found. Terminating process.")

def main():
    global listOfUsers
    while True:
        #Greet the user and present them with the available options
        print("\nWelcome to the main menu. (Enter a number from the options below)")
        print("\t1. Login as an existing user")
        print("\t2. Password recovery")
        print("\t3. Create a new account")
        print("\t4. Exit")

        '''
        For debugging purposes, prints the current list of users along with all their details
        for obj in listOfUsers:
            print(obj.username, obj.password, round(obj.accountBalance, 2), obj.SecurityColor)'''

        while True:
            #Prompt the user to choose something
            userInput = input("You entered: ")

            #Login for existing users
            if userInput == "1":
                print("\nBeginning login process...")
                loginProcess()

                #Return to main menu after login process is complete
                break
            
            #Password recovery for existing users
            elif userInput == "2":
                print("\nBeginning password recovery process...")
                mainPasswordRecovery()

                #Return to main menu after password recovery is complete
                break

            #Account creation
            elif userInput == "3":
                print("\nBeginning account creation...")
                newAccountCreation()
                
                #Return to main menu after account creation is complete
                break

            #Exit the program        
            elif userInput == "4":
                print("\nExiting program...")
                print("Thank you for using our program. Have a nice day! =)")
                quit()

            #Invalid input, reprint the menu
            else:
                print("Invalid input. Reprinting main menu.")
                break

"""For debugging purposes, adds a user named Billy Bob with the password 4444 and color "purple"
listOfUsers.append(UserAccount("Billy Bob", 4444, "purple"))"""
#Run the program and pray it works
main()