#start_chat() definition
from friends import add_friends, friend_list;
status_message=["Janghel!! Kunal Janghel.","OO7","Hey! there im using python"];
def start_chat(spy):
    menu();
    choice = int(raw_input("your choice:"));
    while(choice != 5):
        if (choice == 1):
            cur_status= None ;
            cur_status=add_status(cur_status)
            print "result: "+cur_status;
        elif (choice == 2):
            add_friends();
            print friend_list;
        else:
            print "wrong choice try again"
        menu();
        choice = int(raw_input("your choice:"));

def menu():
    print "Choose from the following options:"
    print "1. Add a status Update"
    print "2. Add Friends"
    print "3. View Messages"
    print "4. Read messages"
    print "5. Exit"

def add_status(current_status):
    ch=int(raw_input("Use 1 to select from previous status and 2 for new status"));
    if(ch==1):
        pos=1
        for i in status_message:
            print pos,". "+i;
            pos=pos+1;
        msg_select=int(raw_input("Please select your message from above:"))
        if(msg_select<pos):
            return "changed status is: "+status_message[msg_select-1];
        else:
            return "Wrong choice:"
    elif(ch==2):
        new_status = raw_input("Enter your new status");
        status_message.append(new_status);
        return "changed status: "+new_status;
    else:
        return "Wrong choice"

