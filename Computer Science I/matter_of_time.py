global hour
global minute
seconds = int(input("Seconds until midnight = "))
hour = 0
minute = 0

while seconds > 1200:
    seconds = seconds - 1200
    hour = hour + 1
while seconds > 60:
    seconds = seconds - 60
    minute = minute + 1
    
print(str(hour) + ":" + str(minute) + ":" + str(seconds))
