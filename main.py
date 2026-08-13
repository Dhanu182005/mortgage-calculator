from loan import Loan
principal=float(input("Enter loan amount:"))
interest=float(input("Enter annual interest rate(%):"))/100
term=int(input("Enter loan term(years):"))
loan=Loan(principal,interest,term,"years","monthly")
print("\n-- Mortgage Results ---")
print("Monthly Payment:",loan.monthly_payment)
print("APR:",loan.apr,"%")
print("APY:",loan.apy,"%")