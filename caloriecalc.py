import FreeSimpleGUI as sg


activity_data = [
    ["Sedentary (Little/no exercise)", 1.2],
    ["Lightly Active (1–3 days/week)", 1.375],
    ["Moderately Active (3–5 days/week)", 1.55],
    ["Very Active (6–7 days/week)", 1.725],
    ["Super Active (Physical job/training)", 1.9]
] # used to calculate BMI of person to be used in caloric calculator

def caloric_intake(age,weight,user_choice,height,sex,): #Set parameters to be passed into the function
    if age < 18: #If the person is too young they cannot use the service
        print('You need to be 18 to use this service') # returns message if user is under 18 and exits program
        return # ends program
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

layout = [
    [sg.Text('Enter Your Age')],
    [sg.InputText(key='-AGE-')],
    [sg.Text('Enter your Weight')],
    [sg.InputText(key='-WEIGHT-')],
    [sg.Text('How active are you?')],
    [sg.InputText(key='-ACTIVE-')],
    [sg.Text('How Tall are you?')],
    [sg.InputText(key='-HEIGHT-')],
    [sg.Text('What sex are you?')],
    [sg.InputText(key='-SEX-')],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window('Begainners', layout)
event, values = window.read()


age = int(values['-AGE-'])
weight = float(values['-WEIGHT-'])
user_choice = values['-ACTIVE-']
height = int(values['-HEIGHT-'])
sex = values['-SEX-']

calculated = caloric_intake(age, weight, user_choice, height, sex)

sg.popup('Your maintainence  calories is', calculated)
window.close()









