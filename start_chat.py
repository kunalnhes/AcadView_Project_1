#start_chat() definition
def start_chat(name, age, rate):
    menu();
    choice = int(raw_input("your choice:"));
    while(choice != 5):
        if (choice == 1):
            cur_status= None ;
            new_status=add_status(cur_status)
        else:
            print "wrong choice try again"
        menu();
        choice = int(raw_input("your choice:"));

def menu():
    print "Choose from the following options:"
    print "1. Add a status Update"
    print "2."
    print "3."
    print "4."
    print "5. Exit"

def add_status(current_status):
    ch=int(raw_input("Use 1 to select from previous status and 2 for new status"));
    if(ch==1):
        print "hello"
    elif(ch==2):
        new_status = raw_input("Enter your new status");
        return new_status;
    else:
        print "Wrong choice"

