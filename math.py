numbers = input("please input three numbers seperated by , \n")
list = numbers.split(",")

def floor(list):
    lowest_number = min(list)
    print("Lowest number = " + str(lowest_number))
    
print(floor(list))

def median(list):
    numbers = []
    one = int(list[0])
    two = int(list[1])
    three = int(list[2])
    numbers.append(one)
    numbers.append(two)
    numbers.append(three)
    median = round((sum(numbers) / len(numbers)), 2)
    print("MEDIAN = " + str(median))
    
print(median(list))
