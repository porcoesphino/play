#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

yearly = np.array(range(1, 90000, 1000))

#http://www.pwc.com/kr/en/publications/korean-tax_2013.jhtml
#http://www.korea4expats.com/article-income-taxes.html
kr_upper = np.array([12000, 46000, 88000, np.nan])
kr_rate = np.array([6, 16, 25, 35])
kr_rate += kr_rate / 10.0

kr_flat = 17
kr_magic = 3.3

#http://www.ato.gov.au/Rates/Individual-income-tax-rates/
au_upper = np.array([18200, 37000, 80000, 180000, np.nan])
au_rate = np.array([0, 19, 32.5, 37, 45])

def calc_tax(largest, smallest, percent):
	return (largest - smallest) * percent / 100.0

def get_actual(amount, upper, rate):

	tax = 0
	prev_limit = 0

	braket = 0
	while (True):
		limit = upper[braket]
		if (amount > limit):
			tax += calc_tax(limit, prev_limit, rate[braket])
		else:
			tax += calc_tax(amount, prev_limit, rate[braket])
			break
		braket += 1
		prev_limit = limit
	return amount - tax

kr_actual = np.array([ get_actual(amount, kr_upper, kr_rate) for amount in yearly ])
au_actual = np.array([ get_actual(amount, au_upper, au_rate) for amount in yearly ])

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(yearly, kr_actual / 52.0)
ax.plot(yearly, (yearly - yearly*kr_flat / 100.0) / 52.0)
ax.plot(yearly, (yearly - yearly*kr_magic / 100.0) / 52.0)
ax.plot(yearly, au_actual / 52.0)

plt.xlabel("Yearly Taxable Income")
plt.ylabel("Weekly In Pocket")

ax.legend(("Korea", "Korea Flat", "Korean Magical", "Australia"), loc=2)

plt.show()
