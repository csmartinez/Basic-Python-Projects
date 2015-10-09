cost = input("How much was your meal?\n")
fraction = input("What fraction of your meal would you like to add to the total as a tip?\n")
    
def total_meal_cost(cost, fraction):
    cost = float(cost)
    percentage = eval(fraction)
    return round((cost * percentage) + cost)

print("\nYour total is $" + str(total_meal_cost(cost, fraction)))

def first_middle_last(lst):
    first = ("First = " + str(lst[0]))
    middle = (len(lst))//2
    middle = lst[middle]
    middle = ("Middle = " + str(middle))
    last = ("Last = " + str(lst[-1]))
    return (first, middle, last)
    
print(first_middle_last(["How", "Low", "Can", "You", "Go"]))

name = input("Enter your friend's name ")
fav_color = input("Enter your friend's favorite color ")
hometown = input("Enter your friend's hometown ")
dob = input("Enter your friends date of birth MM-DD-YYYY ")

def friend_store(name, fav_color, hometown, dob):
    friend = {dob:{"Name":name,"Favorite Color":fav_color,"Hometown":hometown}}
    return friend[dob]

print(friend_store(name, fav_color, hometown, dob))

def reverse_string(string):
    string = string[::-1]
    string = list(string)
    string = " ".join(string)
    return string

print(reverse_string("hello"))

def date_converter(date):
    date = date.split("-")
    month = date[0]
    day = date[1]
    year = date[2]

    months = {"01":"January",
              "02":"Febuary",
              "03":"March",
              "04":"April",
              "05":"May",
              "06":"July",
              "07":"June",
              "08":"August",
              "09":"September",
              "10":"October",
              "11":"November",
              "12":"December" }
    written_month = months[month]
    return(written_month + " " + day + ", " + year)

print(date_converter("01-31-2001"))

