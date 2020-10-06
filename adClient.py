import rpyc
import datetime

AD_SERVER_IP = '172.16.1.5'
AD_BOT_PORT = 19961
domain_controller = 'DC=server, DC=infrastructure, DC=com'
users_org_unit = 'OU=All, OU=Employee, {}'.format(domain_controller)
groups_org_unit = 'OU=Employee_Groups, {}'.format(domain_controller) 

def send_command(command):
    try:
        connection = rpyc.connect(AD_SERVER_IP, AD_BOT_PORT)
        connection.root.run_command(command)
    except Exception as Error:
        print('\nThere is a error in the send command:', str(Error))

def create_user(username, firstname, lastname, password, active=False):

    if active:
        disabled = 'no'
    else:
        disabled = 'yes'

    description = "User added by AD BOT on  {}".format(datetime.datetime.now())
    display_name = lastname + ', ' + firstname

    dn = '"CN={},{}"'.format(username, users_org_unit)
    groups = '"cn=All,{}"'.format(groups_org_unit)

    command = 'dsadd user ' \
              '{} ' \
              '-samid "{}" ' \
              '-upn "{}" ' \
              '-fn "{}" ' \
              '-ln "{}" ' \
              '-display "{}" ' \
              '-desc "{}" ' \
              '-disabled {} ' \
              '-pwd {} ' \
              '-pwdneverexpires yes ' \
              '-mustchpwd no ' \
              '-memberof {} ' \
              '-acctexpires never ' \
              ''.format(
                dn,
                username,
                username,
                firstname,
                lastname,
                display_name,
                description,
                disabled,
                password,
                groups,
                )
    send_command(command)

def manage_user(username, mode):
    dn = '"CN={},{}"'.format(username, users_org_unit)
    cmd = ''

    if mode == 'disable':
        cmd = 'dsmod user {} -disabled yes'.format(dn)
 
    elif mode == 'enable':
        cmd = 'dsmod user {} -disabled no'.format(dn)

    elif mode == 'delete':
        cmd = 'dsrm -noprompt "cn={},{}"'.format(username, users_org_unit)

    send_command(cmd)

def user_password_change(username, new_password):

    dn = 'CN={},{}'.format(username, users_org_unit)
    cmd = 'dsmod user "{}" -pwd {}'.format(dn, new_password)
    send_command(cmd)

def group_user(group_name, mode, username):
    dn = 'CN={},{}'.format(username, users_org_unit)
    cmd = ''
    if mode == 'add':
        cmd = 'dsmod group "cn={},{}"' \
              ' -addmbr "{}"'.format(group_name, groups_org_unit, dn)

    elif mode == 'remove':
        cmd = 'dsmod group "cn={},{}"' \
              ' -rmmbr "{}"'.format(group_name, groups_org_unit, dn)

    send_command(cmd)
