import termcolor
from termcolor import colored
import os

file = None

def input_error():       #INPUT ERROR
    print(colored("Invalid Input!","red"))

def load():              #LOAD THE FILES
    global file
    n = 0
    files = [os.path.join(os.getcwd(), f) for f in os.listdir(os.getcwd()) if f.endswith('.txt')]
    
    if not files:
        print(colored("No text files found in the current directory.", "yellow"))
        return
    print(colored("\nYour Files", "green", attrs=['bold']))
    for f in files: 
        n += 1
        s = f.strip()
        print(colored(str(n) + " - " + os.path.basename(s)))
    print()
    
    while True:
        choice = input(f"Please Select File (1 - {len(files)}): ")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(files):
                file = open(f"{files[choice - 1]}", "r")
                print(colored("File Selected!", attrs=["bold"]))
                break
            else:
                if choice == 0:
                    print(colored("Exiting", "yellow"))
                    break
                else:
                    print("Invalid Index!")
        else:
            input_error()
       
def replace():          #REPLACE WORDS
    global file
    if file == None:
        load()
        if file != None:
            replace()
    file_name = file.name
    file.seek(0)
    content = file.read()
    print(colored("\nNOTE: This operation is case sensitive!","yellow"))
    old=input("\nEnter Word To Be Replaced: ")
    new=input("Enter New Word: ")
    updated_content = content.replace(old, new)
    f = open(file_name, "w")
    f.write(updated_content)
    file = open(file_name,"r+")
    print(colored("Replaced Sucessfully!","green"))
    
def appendtext():          #APPENDS TO A NEW LINE
    global file
    if file == None:
        load()
        if file != None:
            appendtext()
    file = open(file.name, "a")
    new_content=input("Enter Content To Be Added To The End: ")
    file.write("\n" + new_content)
    print(colored("Written Successfully","green"))
    file.close()
    file = open(file.name,"r+")
    
                                              
def edit():               #EDIT FILE
    if file == None:
        load()
        if file != None:
            edit()
    else:
        while True:
            print()
            print("0 - Exit")
            print("1 - Replace Word") 
            print("2 - Add Content In New Line")  
            choice = input("Enter Your Choice (0 - 3): ")     
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    print(colored("Exiting","yellow"))
                    break
                elif choice == 1:
                    replace()
                elif choice == 2:
                    appendtext()
                else:
                    print(colored("No index found!","yellow"))
            else:
                input_error() 

def read():               #READ THE FILES
    if file == None:
        load()
        if file != None:
            read()
    else:
        print(colored(f"\n{os.path.basename(file.name)} Content","cyan",attrs=["bold"]))
        content = file.read()
        print(content)

def create():             #CREATE NEW FILE
    global file
    name = input("Enter File Name: ")
    if not name.endswith(".txt"):
        name += ".txt"
    f = open(name,"w")
    print(colored(f"Created File {name}","yellow"))
    f.close()
    file = open(name, "r+")
    
def clear():              #CLEAR FILE
    global file
    if file == None:
        load()
        if file != None:
            clear()
    else:
        confirmation = input(colored(f"Are you sure you want to clear {os.path.basename(file.name)}, This process is irreversible (yes/no): ","red"))
        if confirmation.lower() == 'yes':
            file_name = file.name
            file.close()
            file = open(file_name,"w")
            file.close()
            file = open(file_name,"r+")
            print(colored("File cleared sucessfully","green"))
        else:
            print(colored("Cancelling!","yellow"))
    
def delete():             #DELETE FILE
    global file
    if file == None:
        load()
        if file != None:
            delete()
    else:
        confirmation = input(colored(f"Are you sure you want to delete {os.path.basename(file.name)}, This process is irreversible (yes/no): ","red"))
        if confirmation.lower() == 'yes':
            file_name = file.name
            file.close()
            os.remove(file_name)
            file = None
            print(colored("File deleted sucessfully","green"))
        else:
            print(colored("Cancelling!","yellow"))            
                            
def menu():                #MENU
    while True:
        print()
        print(colored("1 - View File(s)",attrs=["bold"]))
        print(colored("2 - Read File",attrs=["bold"]))
        print(colored("3 - Create New File",attrs=["bold"]))
        print(colored("4 - Edit File",attrs=["bold"]))
        print(colored("5 - Clear File",attrs=["bold"]))
        print(colored("6 - Delete File",attrs=["bold"]))
        choice=input("Enter Choice (0-5): ")
        if choice.isdigit():
            choice=int(choice)
            if choice == 0:
                print(colored("See You Again!","yellow"))
                break
            elif choice == 1:
                load()
            elif choice == 2:
                read()
            elif choice == 3:
                create()
            elif choice == 4:
                edit()
            elif choice == 5:
                clear()
            elif choice == 6:
                delete()
        else:
            input_error()
menu()