import time

socialmedia = {}

def update(username, status, audience):
    timestamp = time.time()
    status_id = (username + str(timestamp))
    
    if username in socialmedia:
        socialmedia[username].update({status_id:{"Status":status, "Timestamp":timestamp, "Audience":audience, "Likes":0}})
    else:
        socialmedia.update({username:{status_id:{"Status":status, "Timestamp":timestamp, "Audience":audience, "Likes":0}}})

    print("Post made at " + str(timestamp) + " by " + username)
    return status_id

#def like(status_id, username):
    
#def unlike(status_id, username):

def display(status_id, username):
    print("-----")
    print("Time: " + str(socialmedia[username][status_id]["Timestamp"]))
    print("Groups: " + str(socialmedia[username][status_id]["Audience"]))
    print("Likes: " + str(socialmedia[username][status_id]["Likes"]))
    print(str(username) + " (mention with @" + str(username) + ") says: ")
    print(str(socialmedia[username][status_id]["Status"]))

barnabas_one = (update("BarnabasCollins", "Storming the village at 9. Anyone interested?", ["Zombies", "Vampires"]))
time.sleep(1)
casper_one = (update("Casper", "Can I come?", ["Vampires"]))
time.sleep(1)
barnabas_two = (update("BarnabasCollins", "Forgot to include the ghosts! LOL", ["Ghosts"]))
time.sleep(1)
barnabas_three = (update("BarnabasCollins", "Lots of villagers with forks here...", ["Ghosts", "Zombies","Vampires"]))

#like(barnabas_one, "BarnabasCollins")
#like(barnabas_one, "BarnabasCollins")
#like(barnabas_one, "BarnabasCollins")
#like(casper_one, "Casper")
#like(casper_one, "Casper")
#like(casper_one, "Casper")
#like(casper_one, "Casper")
#like(casper_one, "Casper")
#like(barnabas_two, "BarnabasCollins")
#like(barnabas_three, "BarnabasCollins")
#like(barnabas_three, "BarnabasCollins")
#like(barnabas_three, "BarnabasCollins")

#unlike(casper_one, "BarnabasCollins")
#unlike(barnabas_three, "BarnabasCollins")
#unlike(casper_one, "BarnabasCollins")

display(barnabas_one, "BarnabasCollins")
display(barnabas_three, "BarnabasCollins")
display(casper_one, "Casper")
