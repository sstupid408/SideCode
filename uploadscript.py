'''
from firebase import firebase
import pandas as pd

firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

# read in csv data
df = pd.read_csv('data.csv')

# edits data to add gender and age range columns
# genders = []
# ages = []

for index, row in df.iterrows():
    i = 0
    row_genders = ''
    row_ages = []
    if 'men' in row['Restrictions'].lower() and 'women' not in row['Restrictions'].lower():
        row_genders = 'Men'
    if 'women' in row['Restrictions'].lower():
        row_genders = 'Women'
    if 'men/women' in row['Restrictions'].lower():
        row_genders = 'Any'
    if 'children' in row['Restrictions'].lower():
        row_ages.append('Children')
    if 'young adults' in row['Restrictions'].lower():
        row_ages.append('Young adults')
    if 'families w/ newborns' in row['Restrictions'].lower():
        row_ages.append('Families w/ newborns')
    if 'anyone' in row['Restrictions'].lower():
        row_ages.append('Anyone')
    data = {"shelterName": row[1],
            "capacity": row[2],
            "restrictions": row[3],
            "longitude": row[4],
            "latitude": row[5],
            "address": row[6],
            "specialNotes": row[7],
            "phoneNumber": row[8],
            "gender": row_genders,
            "ageRange": row_ages}

    firebase.patch("/Shelters/Shelter_Number_%02d" % i, data)
    i += 1
    
    
    genders.append('Any') if row_genders == '' else genders.append(row_genders)
    ages.append(['Any']) if row_ages == [] else ages.append(row_ages)

df['Gender'] = genders
df['Age Range'] = ages


# send data to firebase
data = df.drop(['Unique Key'], axis=1).to_json()
ids = df['Unique Key']
firebase.patch("/Shelters/Shelter_Number_%02d" % ids, data)
'''

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