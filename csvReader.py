import csv
import adClient
import PySimpleGUI as GUI
import sys

def csvToAD():
    if len(sys.argv) == 1:
        event, values = GUI.Window('CSV Reader',
                        [[GUI.Text('Select the .csv file you want to upload to Active Directory')],
                        [GUI.In(), GUI.FileBrowse()],
                        [GUI.Open(), GUI.Cancel()]]).read(close=True)
        fname = values[0]
    else:
        fname = sys.argv[1]
    print(event)

        
    if fname:
        with open(fname, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                username = row['username']
                firstname = row['firstname']
                lastname = row['lastname']
                password = row['password']
                adClient.create_user(username, firstname, lastname, password, active=True)

