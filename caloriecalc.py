import FreeSimpleGUI as sg
import random

calculated = 0

activity_data = [
    ["1", 1.2],
    ["2", 1.375],
    ["3", 1.55],
    ["4", 1.725],
    ["5", 1.9]
]

dictionary_of_exercise = {
    'calisthenics': {
        'Push': ['Push-ups', 'Dips', 'Diamond Push-ups', 'Pike Push-ups', 'Pseudo Planche Push-ups', 'Handstand Push-ups'],
        'Pull': ['Pull-ups', 'Chin-ups', 'Australian Pull-ups', 'Wide Grip Pull-ups', 'Knees to Elbows', 'Muscle-ups'],
        'Legs': ['Air Squats', 'Lunges', 'Bulgarian Split Squats', 'Calf Raises', 'Glute Bridges', 'Pistol Squats']
    },
    'weight_training': {
        'Push': ['Bench Press', 'Overhead Press', 'Incline Dumbbell Press', 'Tricep Pushdowns', 'Lateral Raises', 'Chest Flys'],
        'Pull': ['Deadlifts', 'Barbell Rows', 'Lat Pulldowns', 'Bicep Curls', 'Face Pulls', 'Hammer Curls'],
        'Legs': ['Back Squats', 'Leg Press', 'Leg Extensions', 'Hamstring Curls', 'Goblet Squats', 'Romanian Deadlifts']
    }
}


def caloric_intake(age, weight, user_choice, height, sex, ):
    multi = 1.0
    for row in activity_data:
        if row[0] == user_choice:
            multi = row[1]
    if sex == 'Woman':
        BMI = 10 * int(weight) + 6.25 * int(height) - 5 * age - 161
        Maint = BMI * multi
        return Maint
    else:
        BMI = 10 * int(weight) + 6.25 * int(height) - 5 * age + 5
        Maint = BMI * multi
        return Maint




def routine(mon, tue, wed, thur, fri, sat, sun, calisthenics, weight_training):
    days_of_Training = [mon, tue, wed, thur, fri, sat, sun]
    count = 0
    if calisthenics:
        style = 'calisthenics'
    elif weight_training:
        style = 'weight_training'
    else:
        sg.popup('You need to select a style!')

    for day in days_of_Training:
        if day:
            count += 1
    if count <= 2:
        sg.popup('You need to workout at least three times a week')

    elif count == 3:
        push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
        pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
        legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)

        output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
        output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
        output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day)
        sg.popup_scrolled(output, title="3-Day Routine")

    elif count == 4:
        push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
        pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
        legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)
        mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2)

        output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
        output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
        output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day) + "\n\n"
        output += "--- Day 4 (Mixed) ---\n" + "\n".join(mixed_day)
        sg.popup_scrolled(output, title="4-Day Routine")

    elif count == 5:
        push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
        pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
        legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)
        mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2)

        output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
        output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
        output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day) + "\n\n"
        output += "--- Day 4 (Mixed) ---\n" + "\n".join(mixed_day) + "\n\n"
        output += "--- Day 5 (Push) ---\n" + "\n".join(push_day)
        sg.popup_scrolled(output, title="5-Day Routine")

    elif count == 6:
        push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
        pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
        legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)
        mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2)
        second_mix = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2) + random.sample(dictionary_of_exercise[style]['Legs'], 2)

        output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
        output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
        output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day) + "\n\n"
        output += "--- Day 4 (Mixed) ---\n" + "\n".join(mixed_day) + "\n\n"
        output += "--- Day 5 (Full Body) ---\n" + "\n".join(second_mix) + "\n\n"
        output += "--- Day 6 (Push) ---\n" + "\n".join(push_day)
        sg.popup_scrolled(output, title="6-Day Routine")

    elif count == 7:
        push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
        pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
        legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)
        mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2)
        second_mix = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(
            dictionary_of_exercise[style]['Pull'], 2) + random.sample(dictionary_of_exercise[style]['Legs'], 2)
        third_mix = random.sample(dictionary_of_exercise[style]['Legs'], 3)

        output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
        output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
        output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day) + "\n\n"
        output += "--- Day 4 (Mixed) ---\n" + "\n".join(mixed_day) + "\n\n"
        output += "--- Day 5 (Full Body) ---\n" + "\n".join(second_mix) + "\n\n"
        output += "--- Day 6 (Legs Focus) ---\n" + "\n".join(third_mix) + "\n\n"
        output += "--- Day 7 (Push) ---\n" + "\n".join(push_day)
        sg.popup_scrolled(output, title="7-Day Routine")





def bulkcut(calculated, bulk, cut, level_one, level_two, level_three,):
    if calculated == 0:
        sg.popup('You need to use the BMR calculator first')
        return
    if not bulk and not cut:
        sg.popup('You need to select your style first  ')
        return
    if not (level_one or level_two or level_three):
        sg.popup('You need to select an aggressiveness level first')
        return
    if bulk:
        if level_one:
            goal_calories = 300
        elif level_two:
            goal_calories = 500
        elif level_three:
            goal_calories = 750
    elif cut:
        if level_one:
            goal_calories = -300
        elif level_two:
            goal_calories = -500
        elif level_three:
            goal_calories = -750

    sg.popup('Your Calories are ', calculated + goal_calories)


def trackbw(bulk, cut, level_one, level_two, level_three, mon, tue, wed, thu, fri, sat, sun):
    if (bulk or cut) and (
            level_one or level_two or level_three):
        total_weight = 0
        days = [mon, tue, wed, thu, fri, sat, sun]
        for val in days:
            if val == '':
                sg.popup('Please enter a value for each day ')
                return
            total_weight += float(val)
        else:
            average_weight = total_weight / 7
            index_weight = average_weight - float(mon)

            if bulk and level_one:
                if 0.15 <= index_weight <= 0.35:
                    sg.popup('Your Bulk is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))

            elif bulk and level_two:
                if 0.35 <= index_weight <= 0.55:
                    sg.popup('Your Bulk is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))

            elif bulk and level_three:
                if 0.55 <= index_weight <= 1:
                    sg.popup('Your Bulk is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))

            elif cut and level_one:
                if -0.35 <= index_weight <= -0.15:
                    sg.popup('Your Cut is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))

            elif cut and level_two:
                if -0.55 <= index_weight <= -0.35:
                    sg.popup('Your Cut is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))

            elif cut and level_three:
                if -1 <= index_weight <= -0.55:
                    sg.popup('Your Cut is going great! Your average weight is', round(average_weight, 2))
                else:
                    sg.popup('Your weight is not aligned for your current goals! Your average weight is',
                             round(average_weight, 2))
    else:
        sg.popup('You need to use Bulking or cutting calculator first ')

sg.theme('DarkBlue')

BMR = [
    [sg.Text('Enter Your Age')],
    [sg.InputText(key='-AGE-')],
    [sg.Text('Enter your Weight in KG')],
    [sg.InputText(key='-WEIGHT-')],
    [sg.Text('How active are you on a scale of 1-5?')],
    [sg.InputText(key='-ACTIVE-')],
    [sg.Text('How Tall are you in CM?')],
    [sg.InputText(key='-HEIGHT-')],
    [sg.Text('What sex are you?')],
    [sg.InputText(key='-SEX-')],
    [sg.Button('Generate TDEE'), sg.Button('Cancel')]
]

availability = [
    [sg.Text('Would you like to do Calisthenics or Weight Training?'),
     sg.Radio('Calisthenics', 'GOAL', key='-calisthenics-'),
     sg.Radio('Weight Training', 'GOAL', key='-weight_training-')],
    [sg.Text('What days are you available for 2 hours to workout?')],
    [sg.Checkbox('Monday', key='-MONDAY-'), sg.Checkbox('Tuesday', key='-TUESDAY-'),
     sg.Checkbox('Wednesday', key='-WEDNESDAY-'), sg.Checkbox('Thursday', key='-THURSDAY-'),
     sg.Checkbox('Friday', key='-FRIDAY-'), sg.Checkbox('Saturday', key='-SATURDAY-'),
     sg.Checkbox('Sunday', key='-SUNDAY-')],
    [sg.Button('Generate Routine')]  # Changed to sg.Button for consistency
]

goal_layout = [
    [sg.Text('Select your fitness goal:')],
    [sg.Radio('Bulk (Gain Muscle)', "RADIO1", key='-BULK-'), sg.Radio('Cut (Lose Fat)', "RADIO1", key='-CUT-')],
    [sg.Text('How aggressive do you want to be? ')],
    [sg.Radio('Calm ', 'CALORIE ', key='Level_One '), sg.Radio('Slight ', 'CALORIE ', key='Level_Two '), sg.Radio('Very ', 'CALORIE ', key='Level_Three ')],
    [sg.Button('Calculate Macros')]
]

body_weight = [

    [sg.Text('Track your bodyweight daily and enter the values ')],
    [sg.Text('Mon: ', size=(5,1)), sg.InputText(key = '-Monday-', size=(6,1))],
    [sg.Text('Tue: ', size=(5,1)), sg.InputText(key = '-Tuesday-',size=(6,1))],
    [sg.Text('Wen: ', size=(5,1)), sg.InputText(key = '-Wednesday-', size=(6,1))],
    [sg.Text('Thu: ', size=(5,1)), sg.InputText(key = '-Thursday-', size=(6,1))],
    [sg.Text('Fri: ', size=(5,1)), sg.InputText(key = '-Friday-', size=(6,1))],
    [sg.Text('Sat: ', size=(5,1)), sg.InputText(key = '-Saturday-', size=(6,1))],
    [sg.Text('Sun: ', size=(5,1)), sg.InputText(key = '-Sunday-', size=(6,1))],
    [sg.Button('Calculate Average Bodyweight')]


]

layout = [
    [sg.TabGroup([
        [
            sg.Tab('BMR Calculator', BMR),
            sg.Tab('Workout Routine Generator', availability),
            sg.Tab('Bulking or Cutting', goal_layout),
            sg.Tab('Track Bodyweight', body_weight)
        ]
    ])],
]


window = sg.Window('Begainners', layout)













while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    if event == 'Generate TDEE':
        try:
            age = int(values['-AGE-'])
            weight = float(values['-WEIGHT-'])
            user_choice = values['-ACTIVE-']
            height = int(values['-HEIGHT-'])
            sex = values['-SEX-']

            calculated = caloric_intake(age, weight, user_choice, height, sex)
            sg.popup('Your maintenance calories is', calculated)
        except:
            pass

    if event == 'Generate Routine':
        routine(values['-MONDAY-'], values['-TUESDAY-'], values['-WEDNESDAY-'], values['-THURSDAY-'], values['-FRIDAY-'], values['-SATURDAY-'], values['-SUNDAY-'], values['-calisthenics-'], values['-weight_training-'])


    if event == 'Calculate Macros':
        bulkcut(calculated, values['-BULK-'], values['-CUT-'], values['Level_One '], values['Level_Two '], values['Level_Three '])

    if event == 'Calculate Average Bodyweight':
        trackbw(values['-BULK-'], values['-CUT-'], values['Level_One '], values['Level_Two '], values['Level_Three '], values['-Monday-'], values['-Tuesday-'], values['-Wednesday-'], values['-Thursday-'], values['-Friday-'], values['-Saturday-'], values['-Sunday-'])



window.close()
