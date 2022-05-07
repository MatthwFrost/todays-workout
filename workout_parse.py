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

# Reads data from JSON and appends to a list
for i in range(0, len(data[weekday][0]['types'])):
    for workout in data[weekday]:
        workout_list.append(workout['types'][i])
        user_workout = workout['workout_type'] 


# Shuffles the list and appends it to a string to write to a file
shuffle = ""
shuffled_list = random.sample(workout_list, len(workout_list))
for item in shuffled_list:
    shuffle += item + ', 3x10\n'

# TODO: Move message creation to a different file.
message = "Good Morning, today is " + user_workout + "!😎:\n\n" + shuffle + \
        "\n\nThis work out will take: 20 minutes⏰ [average]\n\nGoodluck and \
Enjoy!🙂"

# Writing to the file
workout_file = open("workout_file.txt", "w")
workout_file.write(message)
workout_file.close()

f.close()
