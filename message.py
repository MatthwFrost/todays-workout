from workout_parse import Parse

w_type = Parse.user_workout()
workout = Parse.workout_parse()

# Converts list to string, also doesnt had a new line at the end of list
workout_str = ""
for wrk in workout:
    if wrk == workout[-1]:
        workout_str += wrk
        break

    workout_str += wrk + "\n"


    

message = "Good Moring, today is " + w_type + "!😎:\n\n" + workout_str + \
        "\n\nThis work out will take: 20 minutes⏰"

# Writing to the file
file = open("workout_file.txt", "w")
file.write(message)
file.close()





