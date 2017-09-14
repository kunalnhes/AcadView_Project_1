from spy_details import friend_list
from spy_details_class import Spy_Details
import re
from colorama import init, Fore

init()

nameexpr="^[a-zA-Z]+[\sa-zA-Z]*$";
ageexpr="^[0-9]+$"
ratingexpr="^[0-9]+\.[0-9]+$"


def add_friends():
    sd = Spy_Details();
    sd.clear_chats();
    friends = {
        'name': None,
        'age': None,
        'rating': None,
        'is_online': None,
        'chats':[]
    }
    error="";
    while True:
        new_name = raw_input("Please enter your friends name:")
        if(re.match(nameexpr, new_name, flags=0) != None):
            break
        else:
            print(Fore.RED+"Name can only contain alphabets, name cannot be null and name cannot start with space. Please provide a valid name."+Fore.RESET);
    if len(new_name)<=0 :
        error=error+" "+"Name not entered";
    new_salutation = raw_input("How do you want to address your friend")
    while True:
        new_age = raw_input("Please enter the age:")
        if re.match(ageexpr, new_age, flags=0) != None:
            new_age=int(new_age);
            break
        else:
            print(Fore.RED+"Age can only be a integer. Please re enter your age:"+Fore.RESET);
    if new_age<=12 or new_age>=50:
        error = error+" "+"Age not supported";
    while True:
        new_rating = raw_input("Enter your friends rating:");
        if (re.match(ratingexpr, new_rating, flags=0) != None):
            spy_rating = float(new_rating)
            break
        else:
            print(Fore.RED + "Please provide a rating in decimal format. like 4.0 or 4.4 etc..!" + Fore.RESET);
    if new_rating<2.5:
        error = error+" "+"Rating not provided"
    if(len(error)<=0):
        print "Friend added to the list"
        sd.set_details(new_name,new_salutation,new_age,new_rating,True)
        friend_list.append(sd);
    else:
        print "Not added. Error occured: "+ error;
