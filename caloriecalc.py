import FreeSimpleGUI as sg


activity_data = [
    ["1", 1.2],
    ["2", 1.375],
    ["3", 1.55],
    ["4", 1.725],
    ["5", 1.9]
] # used to calculate BMI of person to be used in caloric calculator

def caloric_intake(age,weight,user_choice,height,sex,): #Set parameters to be passed into the function
    if age < 18: #If the person is too young they cannot use the service
        Maint = 'You need to be 18 to use this service' # returns message if user is under 18 and exits program
        return Maint # ends program

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
    [sg.Text('Enter your Weight')],
    [sg.InputText(key='-WEIGHT-')],
    [sg.Text('How active are you? 1-5?')],
    [sg.InputText(key='-ACTIVE-')],
    [sg.Text('How Tall are you?')],
    [sg.InputText(key='-HEIGHT-')],
    [sg.Text('What sex are you?')],
    [sg.InputText(key='-SEX-')],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

availability = [   [sg.Text('What days are you available')]





]

layout = [
    [sg.TabGroup([
        [sg.Tab('Calorie Calculator', BMR),
         sg.Tab('Other Tool', availability)],
    ])],
]

window = sg.Window('Begainners', layout)
event, values = window.read()

if event == 'cancel':
    window.close()
    exit()


age = int(values['-AGE-'])
weight = float(values['-WEIGHT-'])
user_choice = values['-ACTIVE-']
height = int(values['-HEIGHT-'])
sex = values['-SEX-']

calculated = caloric_intake(age, weight, user_choice, height, sex)

if age >= 18:
    sg.popup('Your maintenance  calories is', calculated, 'calories')
    window.close()
else:
    window.close()








