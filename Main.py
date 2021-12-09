from getpass import getpass
from logging import exception
from mysql import connector
import mysql.connector
from mysql.connector import connect, Error
import os
import requests
from time import sleep
from mysql.connector.errors import DataError

class Auth:
    hos=''
    usr=''
    passwd=''
    dab=''
    @staticmethod
    def Authf():
        Auth.dab=''
        Auth.hos=''
        Auth.usr=''
        Auth.passwd
        try:
            hosc=str(input("Enter the Host or Domain: or exit for Exit\r\n"))
            if hosc=='exit':
                return 0
            usrc=str(input("Enter the username: or exit for Exit\r\n"))
            if hosc=='exit':
                return 0
            passwdc=str(getpass("Enter the paassword: or exit for Exit\r\n"))
            if hosc=='exit':
                return 0
            dabc=str(input("DataBase Name: or exit for Exit\r\n"))
            if hosc=='exit':
                return 0
        except exception as e:
            print(e)
            return 0
        Auth.hos=hosc
        Auth.usr=usrc
        Auth.passwd=passwdc
        Auth.dab=dabc

        

def Connecting1(hos,usr,passwd,db):
    try:
        with connect(
            host=hos,
            user=usr,
            password=passwd,
            database=db
        ) as connection:
            print(connection,"\r\n")
            select_count="SELECT * FROM referrals"
            with connection.cursor() as cursor:
                cursor.execute(select_count)
                result = cursor.fetchall()
            y=0
            for row in result:
                y+=1
                print(row)
            print("\r\n")
            print("the count is: ",y)
    except Error as e:
        #cursor=connector.cursor()
        print(e)
        main()

def Connectings(hos,usr,passwd,db):
    try:
        with connect(
            host=hos,
            user=usr,
            password=passwd,
            database=db
        ) as connection:
            print(connection,"\r\n")
            select_count="show tables"
            with connection.cursor() as cursor:
                cursor.execute(select_count)
                result = cursor.fetchall()
            y=0
            for row in result:
                y+=1
                print(row)
            print("\r\n")
            print("the count is: ",y,"\r\n\r\n")
    except Error as e:
        #cursor=connector.cursor()
        print(e)
        main()

def Connecting2(hos,usr,passwd,db):
    try:
        with connect(
            host=hos,
            user=usr,
            password=passwd,
            database=db
        ) as connection:
            print(connection,"\r\n")
            select_count="SELECT * FROM referrals WHERE referrer_id=37"
            with connection.cursor() as cursor:
                cursor.execute(select_count)
                result = cursor.fetchall()
            y=0
            for row in result:
                
                y+=1
                print(row)
            print("\r\n")
            print("the count is: ",y,"\r\n\r\n")
    except Error as e:
        #cursor=connector.cursor()
        print(e)
        main(0)
    
def Self(hos,usr,passwd,db):
    try:
        with connect(
            host=hos,
            user=usr,
            password=passwd,
            database=db
        ) as connection:
            comm=str(input("Enter your command: \r\n"))
            with connection.cursor() as cursor:
                cursor.execute(comm)
                result = cursor.fetchall()
            try:
                x=str(input("Do you wanna to save the results in a text file: yes/no \r\n"))
            except Exception as e:
                print("Enter a valid value in small letters: \r\n")
            if x=='yes':
                try:
                    y=str(input("Enter the path you would Like: "))
                    z=str(input("The file name: "))
                    text_file=open(y+'/'+z,'w')
                    text_file.write(comm)
                    
                    print("\r\n ****Writing Results in the file****** \r\n")
                    
                except Exception as e:
                    print("Note saving results only available for linux and macos\r\n")
                    print("You can see the results if you clicked on\r\n")
                    print(e+'\r\n')
            y=0
            for row in result:
                y+=1
                print(row)
                text_file.write(str(result))
            x=str(input("Continue? yes/no"))
            if x=='yes' or 'y':
                Self(Auth.hos,Auth.usr,Auth.passwd,Auth.dab)
            print("\r\n")
            print("the count is: ",y,"\r\n\r\n")
            text_file.close()
    except Error as e:
        #cursor=connector.cursor()
        print(e)
        main()

def main():
    url = "http://www.google.com"
    timeout = 5
    try:
	    request = requests.get(url, timeout=timeout)
	    print("Connected to the Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
	    print("No internet connection.")
    c=Auth()
    c.Authf()
    if c.hos=='' or c.passwd=='' or c.usr=='' or c.dab=='':
        return 0
    try:
        x=int(input('Using the the Ready commands? Enter 1 for yes or 2 for no \r\n'))
    except Exception as e:
        print(e)
    if x==1: 
        print("\r\n ********************Tables*************************\r\n")
        Connectings(Auth.hos,Auth.usr,Auth.passwd,Auth.dab)
        print("\r\n\r\n ******************Filter 1**********************\r\n")
        Connecting1(Auth.hos,Auth.usr,Auth.passwd,Auth.dab)
        print("\r\n\r\n **************Filter 2******************\r\n")
        Connecting2(Auth.hos,Auth.usr,Auth.passwd,Auth.dab)
        print('\r\n **************END*****************\r\n')
        main()
    if x==2:
        Self(Auth.hos,Auth.usr,Auth.passwd,Auth.dab)
        main()
        
    


if __name__== "__main__":
    main()
