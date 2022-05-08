'''
TODO: 

    - Improve the message creation process                    REMOVED
    - Remove the hard coded 5                                 DONE
    - Could be 1 min sets, not always 3x10
    - A message that has something to do with the work out    REMOVED
    - Make work out random                                    DONE
    - Use the day to fetch the right workout                  DONE
    - Find a way to fetch the right work outs,
      right day, remove the week day  
'''

import json
from random import sample
from datetime import datetime

weekday = datetime.today().strftime('%A')
f = open('data/workouts.json')
data = json.load(f)

class Parse:
    """Takes data from the .json file and makes it availble to use"""
    
    # Takes the work out type
    def user_workout():
        return data[weekday][0]['workout_type']

    # Gets list of type of exersise 
    def workout_parse():
        workout_list = []

        # Reads data from JSON and appends to a list
        for i in range(0, len(data[weekday][0]['types'])):
            for workout in data[weekday]:
                workout_list.append(workout['types'][i])

        # Shuffles the list and appends it to a string to write to a file
        shuffled_list = sample(workout_list, len(workout_list))

        return shuffled_list 


f.close()

