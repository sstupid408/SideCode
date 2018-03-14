from firebase import firebase
import csv
firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

with open('data.csv', 'r') as fin:
    csvin = csv.reader(fin)
    myList = [line for line in csvin]

for sublist in myList[1:]:
    row_genders = ''
    row_ages = []

    if 'women' in sublist[3].lower():
        row_genders = 'Women'
    else:
        if 'men' in sublist[3].lower():
            row_genders = 'Men'
        else:
            row_genders = 'All'

    if 'young adults' in sublist[3].lower():
        row_ages.append('Young adults')
    if 'families' in sublist[3].lower():
        row_ages.append('Families')
    else:
        if 'children' in sublist[3].lower():
            row_ages.append('Children')
    if 'anyone' in sublist[3].lower():
        row_ages.append('Anyone')
    if not ('young adults' in sublist[3].lower() or 'families' in sublist[3].lower() or 'children' in sublist[3].lower()):
        row_ages.append('Anyone')

    data = {"name": sublist[1],
            "capacity": sublist[2],
            "currentCapacity": sublist[2],
            "restrictions": sublist[3],
            "longitude": sublist[4],
            "latitude": sublist[5],
            "address": sublist[6],
            "specialNotes": sublist[7],
            "phoneNumber": sublist[8],
            "gender": row_genders,
            "ageRange": row_ages}
    firebase.patch("/Shelters/" + sublist[1], data)
