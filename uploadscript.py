from firebase import firebase
import csv
firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

with open('data.csv', 'r') as fin:
    csvin = csv.reader(fin)
    myList = [line for line in csvin]

for sublist in myList[1:]:
    data = {"name": sublist[1],
            "capacity": sublist[2],
            "restrictions": sublist[3],
            "longitude": sublist[4],
            "latitude": sublist[5],
            "address": sublist[6],
            "specialNotes": sublist[7],
            "phoneNumber": sublist[8]}
    firebase.patch("/Shelters/Shelter_Number_%02d" % (int(sublist[0]),), data)