budget = int(input("Enter your budget"))
ans = "new"
expense = {}
TotalAmount = 0

while ans != "stop":
    name = input("Enter expense name")
    amount = int(input("Enter the expense amount"))
    TotalAmount += amount
    Expense[name]=amount
    ans = input("Enter 'New' to add another expense, or 'stop' to stop entering expense")


for x in Expense:
    print(f"{Expense}: ${Amount}")

print(TotalAmount)

if TotalAmount == budget:
    print("You're on the match with your budget")
elif TotalAmount >= budget:
    print("You're too broke to be spending this amount of money")
else :
    print("Congratulations!!! You're saving")