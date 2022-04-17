from datetime import datetime


date_format = "%m/%d/%Y"
print('Hello Nicholas, this is a Date time caluclator.')
print('Please enter the first date in M/D/Y format.')
d1 = input()
print('Thank you. Please enter the second date.')
d2 = input()
print('Thank you.')
a = datetime.strptime((d1), date_format)
b = datetime.strptime((d2), date_format)
delta = b - a
print(delta.days)
print("Would you like to perform another calculation? Please type Yes or no.")
r = input()

if r == "Yes":
    import dateTimeCalc
else:
    print("thank you")
