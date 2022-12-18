import inspect
import sys
import os


def getdata():
    import dataline
    return dataline.datatime.now()
def log():
    print("choose your client")
client=int(input("1.harry\n 2.rohan\n 3.hammad"))
con=1
if client==1:
    while con==1:
        print("what do you want to log for harry?")
        choice=(int(input("1.diet\n 2.activity")))
        if choice==1:
            f=open("harrydiet.txt","a")
            data=input("what is harry eaten?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        else:
            f=open("harryexcercise.txt","a")
            data=input("how much time harry workout?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        con=int(input("do you want to log more?\n1.yes\n2.no"))
elif client==2:
    while con==1:
        print("what do you want to log for rohan?")
        choice =int(input("1.dirt\n2.activity"))
        if choice==1:
            f=open("rohandiet.txt","a")
            data=input("what has rohan eaten?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        else:
            f=open("rohanexcercise.txt","a")
            data=input("how much rohan worked out?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        con=int(input("do yo want to log more fro rohan\n1.yes\n2.no"))
elif client==3:
    while con==1:
        print("what do you want to log for hammad?")
        choice=int(input("1.diet\n2.excersise"))
        if choice==1:
            f=open("hammaddiet.txt","a")
            data=input("what has hamaad eaten ?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        else:
            f.open("hammadexcercise.txt","a")
            data=input("how much time hammad workout?")
            f.write(str([str(input())])+" "+data+"\n")
            f.close()
        con=int(input("do you  want to log more from hammad?\n1.yes\n2.no"))

def retrieve():
    con=1
    while con==1:
        print("choose your client")
        client=int(input("1.harry\n2.rohan\n3.hammad"))
        if client==1:
            print("what do you want to retrive foe harry")
            choice=int(input("1.diet\n2.activity"))
            if choice==1:
                f=open("harrydiet.txt","r")
                print(f.readlines())
                f.close()
            else:
                f=open("harryexcercise.txt","r")
                print(f.readlines())
                f.close()
        elif client==2:
            print("what do you retrive for rohan?")
            choice=int(input("1.diet\n2.activity"))
            if choice==1:
                f=open("rohandiet.txt","r")
                print(f.readlines())
                f.close()
            else:
                f=open("rohanexcercise.txt","r")
                print(f.readlines())
                f.close()
        elif client==3:
            print("what you want retrive for hammad?")
            choice=int(input("1.diet\n2.activity"))
            if choice==1:
                f=open("hammaddiet.txt","r")
                print(f.readlines())
                f.close()
            else:
                f=open("hammadexcercise.txt","r")
                print(f.readlines())
                f.close()
        con=int(input("do you want retrive any more datails \n1.yes\n2.no"))

    
        
print("welcome to health care management system")
ch=int(input("what do you want to do \n1.log\n2.retrive"))
if ch==1:
    log()
elif ch==2:
    retrieve()
else:
    print("wrong input plese try again")
