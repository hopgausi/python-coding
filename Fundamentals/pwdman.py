#! python3
# Stores passwords - insecure password manage

import pyperclip, sys, secrets

while True:
    passwds = []
    PASSWORDS = dict()
    pin = input("Enter pin: ")
    try:
        if int(pin) == 2121:
            for i in range(4):
                # auto-generate random passwords
                passwds.append(secrets.token_hex(13))

            PASSWORDS['email'] = passwds[0]
            PASSWORDS['dev_to'] = passwds[1]
            PASSWORDS['medium'] = passwds[2]
            PASSWORDS['github'] = passwds[3]

            if len(sys.argv) < 2:
                print('Usage: python pwdman.py [account name]')
                sys.exit()
            else:
                account = sys.argv[1]
                if account in PASSWORDS.keys():
                    pyperclip.copy(PASSWORDS[account])
                    print(f'Password for {account} copied to clipboard successfully!!')
                    sys.exit()
                else:
                    print('Account not in PASSWORDS -- try agin')
                    sys.exit()
        else:
            print('Incorrect pin')
    except ValueError:
        print("Incorect pin-Enter whole numbers only -- try again")
