import requests
import json
import getpass
import os
import shutil
import urllib

def log():
    print("Please Login:\n ")
    url = "http://127.0.0.1:8000/fdaLogin/"
    check = False
    while not check:
        username = input("Username: ")
        password = getpass.getpass('Password:')
        try:
            response = requests.post('http://127.0.0.1:8000/fdaLogin/', data= {'username': username, 'password': password})
        except requests.exceptions.ConnectionError:
            print("connection error")
        check = response.json()['login']
        if check is False:
            print("Incorrect Username or Password, Please try again")
        else:
            global user
            user = username

    print("You have successfully logged in! To logout and sign in with another account, press 3")


def logout():
    log()


def view_reports():
    global user
    url = "http://127.0.0.1:8000/viewReports/"
    response = requests.post(url, data={'user': user})
    all_reports = response.json()['reports']
    print("\nList of all public reports: \n")
    for x in all_reports:
        print(x+"\n")
    while True:
        report = input("To View Full Details enter the id of the report you'd like to display, or enter 'n' to exit: ")
        if report == 'n':
            break
        else:
            url = "http://127.0.0.1:8000/viewOne/"
            r = requests.post(url, data={'id': report, 'user': user})
            print(r.status_code)
            data = r.json()
            for y in data:
                print(y + ": " + data[y])
            print("\n")
            if len(data) == 9:
                download = input ("To download the file press 1, otherwise press any key: ")
                if download == '1':
                    url = "http://127.0.0.1:8000" + data['file']
                    print(url)
                    download_file(url, 'thisWorks.txt')
        print("\n")

def download_file(url, name):
    #download file and encrppt if neceesary
    fullfilename = os.path.join('C:/Users/Neel_Patel/downloads/', name)
    urllib.request.urlretrieve(url, fullfilename)


def encrypt():
    print("encrypt")


def menu():
    print("This is the menu: Press the number associated with your command\n")
    print("1. View All Accessible Reports  2. Encrypt a Report\n3. Logout and Sign in with new user    4. Quit\n")

if __name__=="__main__":
    print("\nThis is the standalone application:\n\n")
    log()
    while True:
        menu()
        x = input("Enter your command: ")
        if x == "1":
            view_reports()
        elif x == "2":
            encrypt()
        elif x == "3" :
            logout()
        elif x == "4":
            break
        else:
            print("\nInvalid Command")

    print("\nScript has been quit")