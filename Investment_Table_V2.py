SENTINEL = 0
year = 1
haveAllData = False
 
balance = float(input("What is your principal amount invested?: "))

principal = balance


while (not haveAllData) :

    interestRate = float(input("What is the interest rate for year " + str(year) + " (in percent)?: "))

    if interestRate == SENTINEL :
        haveAllData = True
    
    else :
        year = year + 1
        balance = balance * (1 + interestRate / 100)
        yearIncomeAverage = (balance - principal) / (year - 1)

print("At the end of ", (year - 1), "years, your investment will be worth ${:.2f}".format(balance))

print("Your average yearly income is ${:.2f}".format(yearIncomeAverage))
