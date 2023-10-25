import numpy as np
import matplotlib.pyplot as plt

principal_amount=10000
payment=0
no_of_years=20
interest_rate=5
simple_interest=list()
compound_interest=list()

for i in range(no_of_years):
    amount=0
    amount+=principal_amount+payment+principal_amount*(i+1)*(interest_rate/100)
    simple_interest.append(amount)
    amount=0

for i in range(no_of_years):
    amount+=principal_amount+payment+principal_amount*(interest_rate/100)
    principal_amount=amount
    compound_interest.append(amount)
    amount=0

years=np.arange(1,no_of_years+1)

# plt.plot(years,simple_interest)
plt.plot(years,compound_interest)
plt.xlabel('Years')
plt.ylabel('Amount')
plt.show()
