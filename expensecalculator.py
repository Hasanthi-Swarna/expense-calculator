#Expense calculator
#For every amount of money spent, it will be counted as "-x"
#For every amount received, it will be counted as "+x"
#At the end of every month, total expenses will be displayed. "Amount received: ", "Amount spent: ".
#If at the end of the month, amount received is more than amount spent, it will display, "Hurray! Profit is "
#If at the end of the month, amount spent is more, it will display, "Oops! More money spent. Amount spent is "

profit = 0
def credit():
    global profit
    n = int(input("Enter amount received: "))
    profit += n
    print("Total money received till now: ",profit)
loss = 0
def debit():
    global loss
    n = int(input("Enter the amount spent: "))
    loss += n
    print("Total money spent till now: ",loss)

def transactions():
    trans = input("Spent(-) or Received(+): ")
    if trans == "-":
        debit()
    elif trans == "+":
        credit()
    else:
        print("Please enter proper input")
        transactions()
    request()

def monthly():
    global profit, loss
    print("Amount received this month: ", profit)
    print("Amount spent this month: ",loss)
    if profit > loss:
        print("Hurray! Profit is ", profit-loss)
    elif profit < loss:
        print("Oops! More money spent. Amount spent is ", loss-profit)
    else:
        print("Money spent and received is balanced.")
    request()

def request():
    req = input("Would you like to continue to the transactions?(y/n): ")
    if req == "y" or req == "Y":
        transactions()
    elif req == "n" or req == "N":
        x = input("Would you like to get the monthly reports? (y/n): ")
        if x == "y" or x == "Y":
            monthly()
        elif x == "n" or x == "N":
            print("Thank you")
            return
        else:
            print("Please enter proper input")
            request()
    else:
        print("Please enter proper input")
        request()

request()