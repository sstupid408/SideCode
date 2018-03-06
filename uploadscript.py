from firebase import firebase
import csv
firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

with open('data.csv', 'r') as fin:
    csvin = csv.reader(fin)
    myList = [line for line in csvin]

for sublist in myList[1:]:
    row_genders = ''
    row_ages = []

    if 'men' in sublist[3].lower():
        row_genders = 'Men'
    if 'women' in sublist[3].lower():
        row_genders = 'Women'
    if 'children' in sublist[3].lower():
        row_ages.append('Children')
    if 'young adults' in sublist[3].lower():
        row_ages.append('Young adults')
    if 'families w/ newborns' in sublist[3].lower():
        row_ages.append('Families w/ newborns')
    if 'anyone' in sublist[3].lower():
        row_ages.append('Anyone')

    data = {"name": sublist[1],
            "capacity": sublist[2],
            "restrictions": sublist[3],
            "longitude": sublist[4],
            "latitude": sublist[5],
            "address": sublist[6],
            "specialNotes": sublist[7],
            "phoneNumber": sublist[8],
            "gender": row_genders,
            "ageRange": row_ages}
    firebase.patch("/Shelters/Shelter_Number_%02d" % (int(sublist[0]),), data)