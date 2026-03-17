import FreeSimpleGUI as sg


activity_data = [
    ["1", 1.2],
    ["2", 1.375],
    ["3", 1.55],
    ["4", 1.725],
    ["5", 1.9]
] # used to calculate BMI of person to be used in caloric calculator

def caloric_intake(age,weight,user_choice,height,sex,): #Set parameters to be passed into the function

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
    [sg.Button('Submit'), sg.Button('Cancel')] #user entries for TDEE calculator
]


availability = [
    [sg.Text('Would you like to do Calisthenics or Weight Training?'), sg.Radio('Calisthenics', 'GOAL', key='-Cali-'), sg.Radio('Weight Training', 'GOAL', key='-WeightTrain-')],
    [sg.Text('What days are you available for 2 hours to workout?')],
    [sg.Checkbox('Monday', key='-MONDAY-'), sg.Checkbox('Tuesday', key='-TUESDAY-'),
     sg.Checkbox('Wednesday', key='-WEDNESDAY-'), sg.Checkbox('Thursday', key='-THURSDAY-'),
     sg.Checkbox('Friday', key='-FRIDAY-'), sg.Checkbox('Saturday', key='-SATURDAY-'),
     sg.Checkbox('Sunday', key='-SUNDAY-')]
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
        window.close()
        break
    if event == 'Submit':
        age = int(values['-AGE-'])
        weight = float(values['-WEIGHT-'])
        user_choice = values['-ACTIVE-']
        height = int(values['-HEIGHT-'])
        sex = values['-SEX-']

        calculated = caloric_intake(age, weight, user_choice, height, sex)
        sg.popup('Your maintenance calories is', calculated)





