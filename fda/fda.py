import requests
import json
import getpass
import os
import shutil
import urllib
from Crypto.Cipher import AES


def log():
    print("Please Login:\n ")
    check = False
    while not check:
        username = input("Username: ")
        password = getpass.getpass('Password:')
        try:
            response = requests.post('http://evening-shelf-33806.herokuapp.com/fdaLogin/', data= {'username': username, 'password': password})
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
    url = "http://evening-shelf-33806.herokuapp.com/viewReports/"
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
            url = "http://evening-shelf-33806.herokuapp.com/viewOne/"
            r = requests.post(url, data={'id': report, 'user': user})
            data = r.json()
            if data[report] == 'Does not exist':
                print('\nBad input-Quit')
                break
            for y in data:
                if y == 'files':
                    for file in data[y]:
                        if file is not None:
                            print("Attached File: " + file.split("/")[-1])
                else:
                    print(y + ": " + data[y])
            print("\n")
            if len(data['files']) != 0:
                download = input ("To download the attached file type the name of it, otherwise press any key: ")
                check = False
                for name in data['files']:
                    if name.split("/")[-1] == download:
                        check = True
                if check:
                    url = "http://evening-shelf-33806.herokuapp.com/media/report/"+ report + "/" + download
                    download_file(url, download, report)
        print("\n")

def download_file(url, name, id):
    #download file and encrppt if neceesary
    # fullfilename = os.path.join('C:/Users/Neel_Patel/downloads/', name)
    urllib.request.urlretrieve(url, name)
    is_encrypted = requests.post("http://evening-shelf-33806.herokuapp.com/getEncrypt/", data={'user':user, 'id':id, 'file':name})
    if is_encrypted.json()['encrypt'] == True:
        decrypt_file(name, b'123456789abcdfgh')

    print("\nDownload Complete!\n")


def encrypt_file(file_name, symmetric_key):
    # iv = Random.new().read(AES.block_size)
    # iv=b'123456789abcdfgh'
    try:
        if (len(symmetric_key.decode()) is 16):
            new_symmetric_key = symmetric_key
        else:
            new_symmetric_key = symmetric_key.decode()
            for x in range(0, 16 - len(symmetric_key)):
                new_symmetric_key = new_symmetric_key + '0'
            new_symmetric_key = new_symmetric_key.encode()
        if (not os.path.isfile(file_name)):
            return False
        iv = new_symmetric_key
        encrypter = AES.new(new_symmetric_key, AES.MODE_CFB, iv)
        with open(file_name, 'rb')as read_file:
            with open(file_name + '.enc', 'wb')as write_file:
                entire_text = read_file.read()
                encrypted_line = encrypter.encrypt(entire_text)
                write_file.write(encrypted_line)
        return True
    except:
        return False

def decrypt_file(file_name, symmetric_key):
    #iv=b'123456789abcdfgh'
    try:
        if (len(symmetric_key.decode()) is 16):
            new_symmetric_key = symmetric_key
        else:
            new_symmetric_key = symmetric_key.decode()
            for x in range(0, 16 - len(symmetric_key)):
                new_symmetric_key = new_symmetric_key + '0'
            new_symmetric_key=new_symmetric_key.encode()
        if(not os.path.isfile(file_name)):
            return False
        elif not file_name[-4:]=='.enc':
            return False
        else:
            iv=new_symmetric_key
            decrypter = AES.new(new_symmetric_key, AES.MODE_CFB, iv)
            new_file_name = file_name[:((len(file_name))-4)]
            with open(file_name, 'rb')as read_file:
                with open('DEC_' + new_file_name, 'wb')as write_file:
                    entire_text=read_file.read()
                    decrypted_line = decrypter.decrypt(entire_text)
                    write_file.write((decrypted_line))
            return True
    except:
        return False


def menu():
    print("This is the menu: Press the number associated with your command\n")
    print("1. View All Accessible Reports  2. Encrypt a File\n3. Logout and Sign in with new user    4. Quit\n")

if __name__=="__main__":
    print("\nThis is the standalone application:\n\n")
    log()
    while True:
        menu()
        x = input("Enter your command: ")
        if x == "1":
            view_reports()
        elif x == "2":
            name = input("input file name: ")
            check = encrypt_file(name, b'123456789abcdfgh')
            if check:
                print("\n Encryption Succeeded!")
            else:
                print("\n Encryption Failed, File does not exist in folder")
        elif x == "3":
            logout()
        elif x == "4":
            break
        else:
            print("\nInvalid Command")

    print("\nScript has been quit")