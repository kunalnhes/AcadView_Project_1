# import statments
from start_chat import start_chat
import re # use for regular expression matching
from spy_details_class import Spy_Details
from colorama import init,Fore

init()

# Predefined expressions for validation purpose such as name cannnot contain digits etc
nameexpr="^[a-zA-Z]+[\sa-zA-Z]*$";
ageexpr="^[0-9]+$"
ratingexpr="^[0-9]+\.[0-9]+$"

# creating object of spy details and storing it in sd object
sd=Spy_Details();

# User is asked for a choice yes or No. if the user presses yes it continues with the default user or else it ask for the details of the new user
print ("Let's get started with Spy Chat" + Fore.RESET)
q=Fore.CYAN+ "Do you want to continue as "+sd.get_salutation()+" "+sd.get_name()+" Y,y or N,n"+ Fore.RESET
existing = raw_input(q);
#if user wants to enter as a new user than start from  here
if(existing.upper() == 'N'):
    error=None
    while True:
        spy_name = raw_input("Please enter your name: ")
        if re.match(nameexpr, spy_name, flags=0) is not None:
            break
        else:
            print(Fore.RED+"Name can only contain alphabets, name cannot be null and name cannot start with space. Please provide a valid name."+Fore.RESET);
    salutation = raw_input("Please enter your salutation: ")
    print "Welcome "+salutation+" "+spy_name
    print "Okay " + spy_name+ "!! I would like to know more about you "
    spy_age = 0;
    spy_rating = 0.0;
    spy_online = False;
    while True:
        spy_age=raw_input("Enter your age: ");
        if re.match(ageexpr, spy_age, flags=0) is not None:
            spy_age=int(spy_age);
            break
        else:
            print(Fore.RED+"Age can only be a integer. Please re enter your age:"+Fore.RESET);
    if (spy_age>12 and spy_age<50):
        print "you are eligible";
        while True:
            spy_rating = raw_input("Enter your rating:");
            if re.match(ratingexpr, spy_rating, flags=0) is not None:
                spy_rating=float(spy_rating)
                break
            else:
                print(Fore.RED+"Please provide a rating in decimal format. like 4.0 or 4.4 etc..!"+Fore.RESET);
        if (spy_rating >= 4.5):
            print "Brilliant Spy.";
        elif (spy_rating >= 3.5 and spy_rating < 4.5):
            print "You are good Spy.";
        elif (spy_rating >= 2.5 and spy_rating < 3.5):
            print "you can do better."
        else:
            error ="You need to work hard.";
        spy_online = True;
    else:
        error= "You are not eligible"
        print spy_age
    if(spy_online==True):
        print "-----------------------------------------------------------------------------------------------------"
    # to print variable we do like:
        # user_name="Kunal Janghel"
        # print "My name is %s" %(user_name);
        #%d for integer
        #%f for float
        #%.2f for flaot with two decimals......
    if(error == None):
        sd.set_details(spy_name,salutation,spy_age,spy_rating,spy_online)
        print Fore.GREEN+"Authentication complete." + Fore.RESET + "\nWelcome " + sd.get_name() + "\n" + "age: ", sd.get_age(), "\nRating: ", sd.get_rating(), "\nOnline: ", sd.get_online();
        start_chat(sd);
    else:
        print (Fore.RED+error+Fore.RESET)
#if user wants to continue with the default user
elif (existing == 'Y' or existing == 'y'):
    print Fore.GREEN+"Authentication complete." + Fore.RESET + "\nWelcome " + sd.get_name() + "\n" + "age: ", sd.get_age(), "\nRating: ", sd.get_rating(), "\nOnline: ", sd.get_online();
    start_chat(sd);
#if user enters characters other than y,Y,n,N! then exit with incorrect input mmessage
else:
    print (Fore.GREEN+"Wrong input"+Fore.RED)