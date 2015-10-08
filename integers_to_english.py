global digit1
digit1 = ""
number = input("Enter a two-digit number : ")

# Values 10 through 19 should be specially handled
if number[0] == "1":
    if number[1] == "0":
        print("Ten")
    elif number[1] == "1":
        print("Eleven")
    elif number[1] == "2":
        print("Twelve")
    elif number[1] == "3":
        print("Thirteen")
    elif number[1] == "4":
        print("Fourteen")
    elif number[1] == "5":
        print("Fifteen")
    elif number[1] == "6":
        print("Sixteen")
    elif number[1] == "7":
        print("Seventeen")
    elif number[1] == "8":
        print("Eighteen")
    elif number[1] == "9":
        print("Nineteen")
        
# Assign the first digit word to a variable to use later so the same code following
# this doesn't have to be re-written for each individual elif statement

elif number[0] == "2":
    digit1 ="Twenty"
elif number[0] == "3":
    digit1 ="Thirty"
elif number[0] == "4":
    digit1 ="Fourty"
elif number[0] == "5":
    digit1 ="Fifty"
elif number[0] == "6":
    digit1 ="Sixty"
elif number[0] == "7":
    digit1 ="Seventy"
elif number[0] == "8":
    digit1 ="Eighty"
elif number[0] == "9":
    digit1 ="Ninety"

# This code will only be run if the number is greater or equal to 20, so the tens
# values will not print an additional number at the end from what's in the ones
if int(number) >= 20:
    if number[1] == "0":
        print(digit1)
    elif number[1] == "1":
        print(digit1 + " One")
    elif number[1] == "2":
        print(digit1 + " Two")
    elif number[1] == "3":
        print(digit1 + " Three")
    elif number[1] == "4":
        print(digit1 + " Four")
    elif number[1] == "5":
        print(digit1 + " Five")
    elif number[1] == "6":
        print(digit1 + " Six")
    elif number[1] == "7":
        print(digit1 + " Seven")
    elif number[1] == "8":
        print(digit1 + " Eight")
    elif number[1] == "9":
        print(digit1 + " Nine")

