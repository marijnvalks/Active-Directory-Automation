import adClient
import PySimpleGUI as GUI


def create_user():
    GUI.theme('Default1')      
    layout = [
        [GUI.Text('Please enter user data')],
        [GUI.Text('Username', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Firstname', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Lastname', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Password', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Activate account', size=(15, 1)),\
        GUI.Checkbox('',default=False)],
        [GUI.Button('Submit'), GUI.Button('Back')]
    ]

    window = GUI.Window('Create new user', layout)
    while True:             
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Back':
            break
        if event == 'Submit':
            print(values[0], values[1], values[2], values[3], values[4])
            adClient.create_user(values[0], values[1], values[2], values[3], values[4])
            window.close()
            create_user()
        
    window.close()

def add_remove_user_group():
    GUI.theme('Default1')      
    layout = [
        [GUI.Text('Please enter user and group data')],
        [GUI.Text('Groupname', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Username', size=(15, 1)), GUI.InputText()],
        [GUI.Radio('Add', "Radio", default=True, size=(10,1)),\
        GUI.Radio('Remove', "Radio")],
        [GUI.Button('Submit'), GUI.Button('Back')]
    ]

    window = GUI.Window('Add/Remove user from group', layout)
    while True:             
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Back':
            break
        if event == 'Submit':
            if values[2] == True:
                addORremove = 'add'
            if values[3] == True:
                addORremove = 'remove'
            adClient.group_user(values[0], addORremove, values[1])
            window.close()
            add_remove_user_group()
        
    window.close()

def change_user_password():
    GUI.theme('Default1')      
    layout = [
        [GUI.Text('Please enter username and new password')],
        [GUI.Text('Username', size=(15, 1)), GUI.InputText()],
        [GUI.Text('Password', size=(15, 1)), GUI.InputText()],
        [GUI.Button('Submit'), GUI.Button('Back')]
    ]

    window = GUI.Window('Change user password', layout)
    while True:             
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Back':
            break
        if event == 'Submit':
            adClient.user_password_change(values[0], values[1])
            window.close()
            change_user_password()
        
    window.close()    

def manage_user():
    GUI.theme('Default1')      
    layout = [
        [GUI.Text('Enter username and select an option')],
        [GUI.Text('Username', size=(15, 1)), GUI.InputText()],
        [GUI.Radio('Enable account', "Radio", default=True, size=(10,1)),\
        GUI.Radio('Disable account', "Radio"),\
        GUI.Radio('Delete account', "Radio")],
        [GUI.Button('Submit'), GUI.Button('Back')]
    ]

    window = GUI.Window('Manage user', layout)
    while True:             
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Back':
            break
        if event == 'Submit':
            if values[1] == True:
                manUser = 'enable'
            if values[2] == True:
                manUser = 'disable'
            if values[3] == True:
                manUser = 'delete'            
            adClient.manage_user(values[0], manUser)
            window.close()
            manage_user()
        
    window.close()