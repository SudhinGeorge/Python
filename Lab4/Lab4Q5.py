# Write a Python program to get days between two dates. Go to the editor 
# Exampe: days between 28/02/2000 and  28/02/2001

from datetime import date
f_date = date(2000, 2, 28)
l_date = date(2001, 2, 28)
delta = l_date - f_date
print(delta.days)