from firebase import firebase
import csv
firebase = firebase.FirebaseApplication("https://cs-2340-project.firebaseio.com")

with open('data.csv', 'r') as fin:
    csvin = csv.reader(fin)
    myList = [line for line in csvin]

for sublist in myList[1:]:
    data = {"Shelter Name": sublist[1],
            "Capacity": sublist[2],
            "Restrictions": sublist[3],
            "Longitude": sublist[4],
            "Latitude": sublist[5],
            "Address": sublist[6],
            "Special Notes": sublist[7],
            "Phone Number": sublist[8]}
    firebase.patch("/Shelters/Shelter_Number_%02d" % (int(sublist[0]),), data)