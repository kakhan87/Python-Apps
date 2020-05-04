principalAmount = float(input("What is your principal amount invested?: "))

annualInterestRate = float(input("What is the annual interest rate (in percent)?: "))

investmentYears = int(input("How many years will this be invested for?: "))                                

print("Year", "  ", "Balance")
for year in range(1, investmentYears+1) :
    balance = principalAmount * ((1 + annualInterestRate/100)**year)
    print(" ", year, "  ", "${:,.2f}".format(balance) )
    
    
    
