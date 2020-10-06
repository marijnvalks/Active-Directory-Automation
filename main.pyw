import adClient
import csvReader
import manageFunction
import PySimpleGUI as GUI


layout = [[GUI.Text('Choose what you want to do')],
          [GUI.Text('')],
          [GUI.Button('Manual create user'), GUI.Button('Change user password')],
          [GUI.Button('Add/Remove user from group'), GUI.Button('Manage user')],
          [GUI.Button('Import .csv file')],
          [GUI.Text('')],
          [GUI.Button('Exit')]
          ]

window = GUI.Window('Active Directory Bot', layout)
 
while True:             
    event, values = window.read()
    if event == GUI.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Manual create user':
        manageFunction.create_user()
    if event == 'Change user password':
        manageFunction.change_user_password()
    if event == 'Manage user':
        manageFunction.manage_user()
    if event == 'Add/Remove user from group':
        manageFunction.add_remove_user_group()
    if event == 'Import .csv file':
        csvReader.csvToAD()

window.close()
