global dollars
global quarters
global dimes
global nickels
pennies = int(input("How many pennies do you have? "))
dollars = 0
quarters = 0
dimes = 0
nickels = 0

while pennies > 100:
    pennies = pennies - 100
    dollars = dollars + 1
while pennies > 25:
    pennies = pennies - 25
    quarters = quarters + 1
while pennies > 10:
    pennies = pennies - 10
    dimes = dimes + 1
while pennies > 5:
    pennies = pennies - 5
    nickels = nickels + 1

print("Your change is " + str(dollars) + " dollars " + str(quarters) + " quarters " + str(dimes) + " dimes " + str(nickels) + " nickels " + str(pennies))
