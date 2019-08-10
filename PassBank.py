#!/usr/bin/python3
#=========================
#import Modules
import os
import sys
import subprocess
#set founctions
def bankadd():
    print ("Please fill out the form below")
    #Get Site or Service of Account
    adds = input ("Enter Account Service Name or Address : ")
    #Get Username
    addu = input ("Please Enter Username : ")
    #Get Password
    addp = input ("Enter Password : ")
    #more ...
    site = "Service : "
    usr = "Username : "
    paas = "Password : "
    ser = (site + adds)
    us = (usr + addu)
    ps = (paas + addp)
    px = ps.encode().hex()
    
    #open File and write information in this

    fin = open("accounts.txt", 'a+')
    fin.write("##########################################")
    fin.write("\n")
    fin.write(ser)
    fin.write("\n")
    fin.write(us)
    fin.write("\n")
    fin.write(px)
    fin.write("\n")
def bankread():
    #open File and Read Informations
    fin1 = open("accounts.txt", 'r')
    a = fin1.read()
    print (a)
def bankde():
    print ('''
    1)Edit with Nano
    2)Edit with vim
    ''')
    #use nano to Delete or edit File :)
    editor = input ("Please Enter Option : ")
    if editor == "1":
        rc = subprocess.call(['which' , 'nano'])
        if rc == 0:
            os.system("nano accounts.txt")
        else :
            print ("nano not installed!!! Please install it & Try again")
    elif  editor == "2" :

        rc = subprocess.call(['which','vim'])
        if rc == 0:
            os.system("vim  accounts.txt")
        else :
            print ("vim not installed!!! Please install it & Try again")
def dec():
    try:
        
        de = input ("Please Enter Encoded Password : ")
        p = bytearray.fromhex(de).decode()
        print(p) 
    except:
        print ("Please Enter the Hex Text....")
while True:
    
    print ('''
    #####################################
    #         Your Password Bank        #
    #                                   #
    #          Created By AMJ_403       #
    #       Licence : GPL-3             #
    #####################################
    1)Add Account to PassBank
    2)View Accuonts
    3)Delete or Edit Account
    4)Decode Password
    00)Exit
    ''')

    Bankop = input ("Please Enter Option : ")
    if Bankop == "1":
        os.system("clear")
        bankadd()
        os.system("python3 PassBank.py")
    if Bankop == "2":
        os.system("clear")
        bankread()
    if Bankop == "3":
        os.system("clear")
        bankde()
    if Bankop == "4":
        os.system("clear")
        dec()
    if Bankop == "00":
        sys.exit()
