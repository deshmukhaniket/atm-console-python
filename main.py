from atmcard import AtmCard

def print_menu():
    print('Please chose from below options: ')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    print('4. Exit')

def Deposit(self):

    try:
        #taking input from user
        deposit = float(input('Enter the amount that you wish to deposit: '))
        #adding the deposited amount to the existing balance
        self.set_balance(self.get_balance() + deposit)
        print('You have successfully deposited the amount', "{0:.2f}".format(deposit) ,'in your account')
    except:
        print('Invalid input! Expecting a number value, please try again. ')

def Withdraw(self):

    try:
        withdraw = float(input('Enter the amount you wish to withdraw: '))
        if (self.get_balance() < withdraw):
            print ('Insufficient balance! Please enter valid withdrawal amount')
        else:
            self.set_balance(self.get_balance()-withdraw)
            print(f'Please collect your withdrawal amount of Rs {withdraw}. Thank you for banking with us!')

    except:
        print('Invalid input! Expecting a number value, please try again. ')

def CheckBalance(self):
    print(self.get_balance())

if __name__ == '__main__':

    current_user = AtmCard('','','','')

    """Need to have some database in order to check
    if the provided data by user matches with the database / repository"""

    listOfCardHolders = []
    listOfCardHolders.append(AtmCard('2222', 2222, 'Ayesha', 150))
    listOfCardHolders.append(AtmCard('1111', 1111, 'Aniket', 150))
    listOfCardHolders.append(AtmCard('1212', 1212, 'Shubham', 150))
    listOfCardHolders.append(AtmCard('3333', 3333, 'Kapil', 150))

    while True:
        try:
            debitCardNum = input('Please enter debit card number associated with your account: ')
            
            for x in listOfCardHolders:
                if x.cardNum == debitCardNum:
                    current_user = x
                    break
            
            
            if current_user != None:
                break

        except:
            print('Invalid Input')
    
    while True:
        try:
            user_pin = int(input('Enter your unique 4 digit security PIN: '))
            if user_pin == x.pin:
                print( 'Welcome', x.fname,)
                break
            else:
                print ('Invalid PIN, please try again')
        except:
            print ('Invalid PIN, please try again')

    # prompt user to select an option

    option = 0

    while option != 4:
        print_menu()
        option = int(input())

        if option == 1:
            Deposit(current_user)
        elif option == 2:
            Withdraw(current_user)
        elif option == 3:
            CheckBalance(x)
        elif option == 4:
            break
        else:
            option = 0
    print ('Thank you for using the bank')