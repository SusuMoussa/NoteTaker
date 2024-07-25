import os
import random
import time

def MakeNote():
    nameofnote = input("Enter Note Name: ")
    nameofnote = "Notes\\" + nameofnote
    con = open(nameofnote, "w")
    
    while True: 
        l = input("Note>")
        if l == "/save":
            break
        con.write(l)
    con.write("\n")
    con.close()

def ReadNote():
    first_note = input("Pick A Note: ")
    first_note = "Notes\\" + first_note
    con = open(first_note, "r")
    print(con.read())
    con.close()

def ListNote():
    notes = "Notes"
    for l in os.listdir(notes):
        print(l)

def RemoveNote():
    QA = input("What File You Want To Delete? :")
    os.remove("Notes\\" + QA)

def HumanType():
    note = input("what note you want to simulate: ")
    controller = open('Notes\\'+note, 'r')
    contents = controller.read()
    for letter in contents:
        print(letter, end="", flush=True)
        delay = random.randint(1, 5) /15
        time.sleep(delay)
    controller.close()

