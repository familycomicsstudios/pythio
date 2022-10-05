import os
import sys
import subprocess
print("PYTHIO CONSOLE")
print("VERSION 0.1.0")
cwd = os.getcwd()
python = "python3"
os.chdir("Games")
while True:
    command = input("PYTHIO> ")
    split = command.split()
    if split[0] == "games":
        games = os.listdir()
        for game in games:
            print(game)
    if split[0] == "play":
        exec(open(split[1]).read())
    if split[0] == "settings":
        print("SETTINGS")
        print("A: PYTHIO SETTNGS")
        cmd2 = input("SETTINGS> ")
        if cmd2.lower() == "a":
            print("PYTHIO SETTINGS")
            print("A: OS")
            cmd3 = input("PYTHIO-SETT> ")
            if cmd3.lower() == "a":
                print("WHAT OS ARE YOU USING")
                print("A: WindowsNT")
                print("B: DOS")
                print("C: Unix")
                cmd4 = input("OS-SETT> ")
                if cmd4.lower() == "a":
                    os = "winnt"
                    print("OS set to WindowsNT")
                if cmd4.lower() == "b":
                    os = "dos"
                    print("OS set to DOS.")
                if cmd4.lower() == "c":
                    os = "unix"
                    print("OS set to Unix.")
            
