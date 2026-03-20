from os.path import join
import FreeSimpleGUI as sg
import random

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

layout = [
    [sg.TabGroup([
        [sg.Tab('Calorie Calculator', BMR),
         sg.Tab('Other Tool', availability)],
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
        days_of_Training = ['-MONDAY-', '-TUESDAY-', '-WEDNESDAY-', '-THURSDAY-', '-FRIDAY-', '-SATURDAY-', '-SUNDAY-']
        count = 0
    if values['-calisthenics-']:
        style = 'calisthenics'
    else:
        style = 'weight_training'

        for day in days_of_Training:
            if values[day]:
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
            mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(dictionary_of_exercise[style]['Pull'], 2)

            output = "--- Day 1 (Push) ---\n" + "\n".join(push_day) + "\n\n"
            output += "--- Day 2 (Pull) ---\n" + "\n".join(pull_day) + "\n\n"
            output += "--- Day 3 (Legs) ---\n" + "\n".join(legs_day) + "\n\n"
            output += "--- Day 4 (Mixed) ---\n" + "\n".join(mixed_day)
            sg.popup_scrolled(output, title="4-Day Routine")

        elif count == 5:
            push_day = random.sample(dictionary_of_exercise[style]['Push'], 3)
            pull_day = random.sample(dictionary_of_exercise[style]['Pull'], 3)
            legs_day = random.sample(dictionary_of_exercise[style]['Legs'], 3)
            mixed_day = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample( dictionary_of_exercise[style]['Pull'], 2)

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
            second_mix = random.sample(dictionary_of_exercise[style]['Push'], 2) + random.sample(dictionary_of_exercise[style]['Pull'], 2) + random.sample(dictionary_of_exercise[style]['Legs'], 2)

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



window.close()




