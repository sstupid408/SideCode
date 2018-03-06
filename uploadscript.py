import firebase
import pandas as pd

firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

# read in csv data
df = pd.read_csv('data.csv')

# edits data to add gender and age range columns
genders = []
ages = []

for index, row in df.iterrows():
    row_genders = ''
    row_ages = []
    if 'men' in row['Restrictions'].lower() and 'women' not in row['Restrictions'].lower():
        row_genders = 'Men'
    if 'women' in row['Restrictions'].lower():
        row_genders = 'Women'
    if 'children' in row['Restrictions'].lower():
        row_ages.append('Children')
    if 'young adults' in row['Restrictions'].lower():
        row_ages.append('Young adults')
    if 'families w/ newborns' in row['Restrictions'].lower():
        row_ages.append('Families w/ newborns')
    if 'anyone' in row['Restrictions'].lower():
        row_ages.append('Anyone')
        
    genders.append('Any') if row_genders == '' else genders.append(row_genders)
    ages.append(['Any']) if row_ages == [] else ages.append(row_ages)
    
df['Gender'] = genders
df['Age Range'] = ages

# send data to firebase
data = df.drop(['Unique Key'], axis=1).to_json()
firebase.patch("/Shelters/Shelter_Number_%02d" % (int(sublist[0]),), data)