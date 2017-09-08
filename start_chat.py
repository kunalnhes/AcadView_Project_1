#start_chat() definition
from read_message import read_message
from send_message import send_message
from spy_details import friend_list
from read_chat import read_chat
import re
from colorama import Fore,init
from add_friend import add_friends

init()

#expression for validation
nameexpr = "^[a-zA-Z0-9]+[\s0-9a-zA-Z]*$";
choexpr = "^[0-9]+$"

status_message=[]


def start_chat(spy):
    cur_status = -1
    menu()
    choice = choose()
    while(choice != 6):
        if (choice == 1):
            if cur_status==-1:
                print "current status is: "+Fore.RED+"NULL"+Fore.RESET
            else:
                print ("Current status is: "+Fore.GREEN+status_message[cur_status-1])+Fore.RESET
            result=str(add_status(cur_status))
            if (re.match(choexpr, result, flags=0) != None):
                cur_status=int(result)
                print ("Status changed. New status is: "+Fore.GREEN+ status_message[cur_status-1])+Fore.RESET
            else:
                print Fore.RED+result+Fore.RESET
        elif (choice == 2):
            add_friends();
            print "Total available friends are: "+str(len(friend_list))
            show_friends();
        elif (choice == 3):
            send_message()
        elif (choice == 4):
            read_message()
        elif(choice == 5):
            read_chat()
        else:
            print Fore.RED+"Wrong Choice Please Try again"+Fore.RESET
        menu();
        choice = choose()

def show_friends():
    pos=1;
    for i in friend_list:
        print pos, ". " + i.get_name();
        pos = pos + 1;


def choose():
    while True:
        choice=raw_input("Enter your choice: ")
        if(re.match(choexpr,choice,flags=0)!=None):
            return int(choice)
        else:
            print (Fore.RED+"Please enter only integer choice."+Fore.RESET)

def menu():
    print "Choose from the following options:"
    print "1. Add a status Update"
    print "2. Add Friends"
    print "3. Send message to a friend"
    print "4. Read message"
    print "5. Read chat history"
    print "6. Close the application"

def add_status(current_status):
    print "\nEnter 1 to choose from the previous status and 2 to add new status: "
    ch=choose()
    if(ch==1):
        pos=1
        for i in status_message:
            print pos,". "+i;
            pos=pos+1;
        if not status_message:
            return "Sorry. No previous history available"
        else:
            msg_select=choose()
            if(msg_select<pos):
                return msg_select;
            else:
                return "Wrong choice"
    elif(ch==2):
        while True:
            new_status = raw_input("Enter your new status: ");
            if(re.match(nameexpr,new_status,flags=0)!=None):
                status_message.append(new_status);
                break
            else:
                print "Please enter some status."
        return len(status_message);
    else:
        return Fore.RED+"Wrong choice"+Fore.RESET