from datetime import date, datetime
from workout_parse import Parse

w_type = Parse.user_workout()
workout = Parse.workout_parse()
username = Parse.username()

weekday = datetime.today().strftime('%A')
today = date.today()
d1 = today.strftime("%d-%m-%Y")

def SMS_send():
    # Converts list to string, also doesnt had a new line at the end of list
    workout_str = ""
    for wrk in workout:
        if wrk == workout[-1]:
            workout_str += wrk
            break
        workout_str += wrk + "\n"

    message = "Good Moring " + username + ", today is " + w_type + "!😎:\n\n" + workout_str + \
            "\n\nThis work out will take: 20 minutes⏰,"

    # Writing to the file
    file_name = "SMSlog/" + weekday +"_"+ d1 + "_" + w_type + ".txt"
    file = open(file_name, "w")
    file.write(message)
    file.close()

    return file_name

print(username)
print(SMS_send())


