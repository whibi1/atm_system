print("********************\nWelcome to ATM menu\n********************")

print("""
Transactions:

1. Balance Inquiry
2. Deposit Money
3. Withdraw Money

You can exit the program with the 'q' key.

""")

balance  = 1000 # Let's say our balance is $1000.

while True:
    Transaction = input("Please enter transaction:")

    if (Transaction == "q"):
        print("We are waiting for you soon :)")
        break
    elif (Transaction == "1"):
        print("Your Balance is {} $".format(balance))
    elif (Transaction == "2"):
        amount = int(input("The amount you want to deposit:"))

        balance += amount
    elif (Transaction == "3"):
        amount = int(input("Please enter the amount you want to withdraw:"))
        if (balance - amount < 0 ):
            print("You cannot withdraw that much money.")
            print("Your Balance is {} $".format(balance))
            continue
        balance -= amount

    else:
        print("Please enter a valid Transaction.")
