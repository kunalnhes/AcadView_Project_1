# import statments
from spy_details import spy
from start_chat import start_chat
import re

print "Let's get started"
q="Do you want to continue as "+spy['salutation']+" "+spy['name']+" Y,y or N,n"
existing = raw_input(q);
nameexpr="^[a-zA-Z]+[\sa-zA-Z]*$";
ageexpr="^[0-9]+$"
ratingexpr="^[0-9]+\.[0-9]+$"
if(existing.upper() == 'N'):
    error=None
    while True:
        spy_name = raw_input("Please enter your name: ")
        if(re.match(nameexpr, spy_name, flags=0) != None):
            break
        else:
            print("Name can only contain alphabets, name cannot be null and name cannot start with space. Please provide a valid name.");
    #Concatenation of salutation with the name and condition checking.
    salutation = raw_input("Please enter your salutation: ")
    spy_name = salutation + " " + spy_name
    print "Welcome "+spy_name
    print "Okay " + spy_name+ "!! I would like to know more about you "
    spy_age = 0;
    spy_rating = 0.0;
    spy_online = False;
    while True:
        spy_age=raw_input("Enter your age: ");
        if re.match(ageexpr, spy_age, flags=0) != None:
            spy_age=int(spy_age);
            break
        else:
            print("Age can only be a integer. Please re enter your age:");
    if (spy_age>12 and spy_age<50):
        print "you are eligible";
        while True:
            spy_rating = raw_input("Enter your rating:");
            if (re.match(ratingexpr, spy_rating, flags=0) != None):
                spy_rating=float(spy_rating)
                break
            else:
                print("Please provide a rating in decimal format. like 4.0 or 4.4 etc..!");
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
        print "Authentication complete. \n Welcome " + spy_name + "\n" + "age: ", spy_age, "\nRating: ", spy_rating, "\nOnline: ", spy_online;
        spy['name'] = spy_name;
        spy['age'] = spy_age;
        spy['rating'] = spy_rating;
        spy['is_online'] = spy_online;
        start_chat(spy);
    else:
        print ""+error
elif (existing == 'Y' or existing == 'y'):
    print "Okay lets get started"
    print "Authentication complete. \nWelcome " + spy['name'] + "\n" + "age: ", spy['age'], "\nRating: ", spy['rating'], "\nOnline: ", spy['is_online'];
    start_chat(spy);
else:
    print "Wrong input";