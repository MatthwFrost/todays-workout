import json

f = open('data/workouttypes.json')
data = json.load(f)

class GetExercise:

    def get_workout(get_type):
        exercise_list = []
        for name in data[get_type]:
            exercise_list.append(name['name'])
        return exercise_list


    def get_difficulty(get_type):
        diff = dict()
        for item in data[get_type]:
            name = item['name']
            difficulty = item['difficulty']
            diff[name] = difficulty
        return diff

    def get_time(get_type):
        time = dict() 
        for item in data[get_type]:
            name = item['name']
            user_time = item['time']
            time[name] = user_time
        return time

#wrk_name = GetExercise.get_workout('back')
print(GetExercise.get_workout('back'))
print(GetExercise.get_difficulty('back'))
print(GetExercise.get_time('back'))
