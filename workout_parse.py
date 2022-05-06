'''
TODO: 

    - Improve the message creation process
    - Remove the hard coded 5                                 DONE
    - Could be 1 min sets, not always 3x10
    - A message that has something to do with the work out
    - Make work out random                                    DONE
    - Use the day to fetch the right workout                  DONE
'''
import json
import random
from datetime import datetime

weekday = datetime.today().strftime('%A')
f = open('workouts.json')
data = json.load(f)
workout_list = []
message = ""

for i in range(0, len(data[weekday][0]['types'])):
    for workout in data[weekday]:
        workout_list.append(workout['types'][i])
        user_workout = workout['workout_type'] 

message += "Good Morning, today is " + user_workout + "!:\n\n"

# Shuffles the list and appends it to a string to write to a file
shuffled_list = random.sample(workout_list, len(workout_list))
for i in shuffled_list:
    message += i + ', 3x10\n'
message += "\n\nEnjoy!"

# Writing to the file
workout_file = open("workout_file.txt", "w")
workout_file.write(message)
workout_file.close()

f.close()
