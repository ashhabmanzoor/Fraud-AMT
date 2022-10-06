import re

x = ['1600,2499', '2500,25000', '25000']

for z in x:
    a = re.split(",", z)
    print(a)
