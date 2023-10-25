def calculate_total_interest(P, r, n):
    r = r / 12 / 100 # Monthly rate
    M = P * r * (1 + r)**n / ((1 + r)**n - 1)
    total_repayment = M * n
    total_interest = total_repayment - P
    print(f"The monthly rate is__________: {r:.5f} %")
    print(f"The monthy payment is________: ₿ {M:.2f}")
    return total_interest

P = float(input("Enter the loan amount_______₿: ")) # Loan amount
r = float(input("Enter the annual rate_____(%): ")) # Annual rate
n = float(input("Enter the loan term in years_: ")) * 12 # Duration in years converted in months
# P = 100000
# r = 5
# n = 20*12
total_interest = calculate_total_interest(P, r, n)
R = (P + total_interest)/P*100

print(f"The total loan amount is_____: ₿ {P:.0f}")
print(f"The annual interest rate is__: {r}%")
print(f"The loan term in years is____: {n/12:.0f}")
print(f"The loan term in months is___: {n:.0f}")
print(f"Total interest paid over term: ₿ {total_interest:.2f}")
print(f"__________________________________________")
print(f" ")
print(f"Total paid over term_________: ₿ {P + total_interest:.2f}")
print(f"Real interest rate over term_: {R:.2f}%")
