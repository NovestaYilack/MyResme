rollover = input("Enter 'account' to create an account, or 'login' to log into your account")

if rollover == "account" :
    name = input("Full Name")
    email = input("Email")
    deposit = int(input("Initial deposit amount"))
    password = input("New password")
    Rpassword = input("Repeat password")
    while password != Rpassword:
        print("The two passwords must match each other. Try again")
        name = input("Full Name")
        email = input("Email")
        deposit = int(input("Initial deposit amount"))
        password = input("New password")
        Rpassword = input("Repeat password")
    print("Account successfully created. Enter your email, then password to Login")
    emal = input("Email")
    psswrd = input("Password")
    while emal == email and psswrd != password :
        print("Wrong password")
        emal = input("Email")
        psswrd = input("Password")
    if psswrd == password :
        print("Successfully logged in")
if rollover == "login" :
    email = input("Email")
    password = input("Password")
    print("Successfully logged in")

else :
    rollover = input("Enter 'account' to create an account, or 'login' to log into to your account")

choice = input("Enter 'deposit' to deposit, 'withdraw' to withdraw, 'check' to check balance, or 'logout' to logout")

if choice == "deposit":
    acct = int(input("Account Number"))
    amount = int(input("Deposit amount"))
    validate = input("enter 'yes' to validate deposit")
    print(f"Successful deposit of ${amount} to your account {acct}")
elif choice == "withdraw":
    acct = int(input("Account Number"))
    amount = int(input("Amount to be withdrawn"))
    pin = int(input("enter your pin to validate withdrawal"))
    print(f"successful withdrawal of {amount} from your account {acct}")
elif choice == "check":
    print("Your account balance is...")
elif choice == "logout":
    break

