#start_chat() definition
from read_message import read_message
from friends import add_friends
from select_friend import select_friend
from send_message import send_message
from spy_details import friend_list
import re
status_message=["Janghel!! Kunal Janghel.","OO7","Hey! there im using python"]
nameexpr="^[a-zA-Z0-9]+[\s0-9a-zA-Z]*$";

def start_chat(spy):
    menu()
    choice = choose()
    while(choice != 5):
        if (choice == 1):
            cur_status= None
            cur_status=add_status(cur_status)
            print "result: "+cur_status;
        elif (choice == 2):
            add_friends();
            print friend_list;
        elif (choice == 3):
            send_message()
        elif (choice == 4):
            read_message()
        else:
            print "wrong choice try again"
        menu();
        choice = choose()

choexpr="^[0-9]+$"
def choose():
    while True:
        choice=raw_input("Enter your choice: ")
        if(re.match(choexpr,choice,flags=0)!=None):
            return int(choice)
        else:
            print "Please enter only integer choice"

def menu():
    print "Choose from the following options:"
    print "1. Add a status Update"
    print "2. Add Friends"
    print "3. Send message to a friend"
    print "4. Read message"
    print "5. Exit"

def add_status(current_status):
    print "\nEnter 1 to choose from the previous status and 2 to add new status"
    ch=choose()
    if(ch==1):
        pos=1
        for i in status_message:
            print pos,". "+i;
            pos=pos+1;
        msg_select=choose()
        if(msg_select<pos):
            return "changed status is: "+status_message[msg_select-1];
        else:
            return "Wrong choice:"
    elif(ch==2):
        while True:
            new_status = raw_input("Enter your new status");
            if(re.match(nameexpr,new_status,flags=0)!=None):
                status_message.append(new_status);
                break
            else:
                print "Please enter some status"
        return "changed status: "+new_status;
    else:
        return "Wrong choice"