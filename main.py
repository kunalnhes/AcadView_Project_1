# import statments
from spy_details import spy
from start_chat import start_chat

print "Let's get started"
q="Do you want to continue as "+spy['salutation']+" "+spy['name']+" Y,y or N,n"
existing = raw_input(q);
if(existing.upper() == 'N'):
    error=None
    spy_name = raw_input("Please enter your name: ")
    #Concatenation of salutation with the name and condition checking.
    if len(spy_name)>0:
        salutation = raw_input("Please enter your salutation: ")
        if len(salutation)>0:
            spy_name = salutation + " " + spy_name
            print "Welcome "+spy_name
            print "Okay " + spy_name+ "!! I would like to know more about you "
            spy_age = 0;
            spy_rating = 0.0;
            spy_online = False;

            spy_age = int(raw_input("Enter your age:"));
            print type(spy_age);
            if spy_age>12 and spy_age<50:
                print "you are eligible";
                spy_rating = float(raw_input("Enter your rating:"));
                if (spy_rating >= 4.5):
                    print "Brilliant Spy.";
                elif (spy_rating >= 3.5 and spy_rating < 4.5):
                    print "You are good Spy.";
                elif (spy_rating >= 2.5 and spy_rating < 3.5):
                    print "you can do better."
                else:
                    error ="You need to work hard.";
                sspy_online = True;
            else:
                error= "You are not eligible"
            if(spy_online==True):
                print "-----------------------------------------------------------------------------------------------------"
        else:
            error= "You did not entered your salutation. Please retry!"

    else:
        error= "You did not entered your name. Please retry!"
    # to print variable we do like:
        # user_name="Kunal Janghel"
        # print "My name is %s" %(user_name);
        #%d for integer
        #%f for float
        #%.2f for flaot with two decimals......
    if(error == None):
        print "Authentication complete. Welcome " + spy_name + "\n" + "age: ", spy_age, "\nRating: ", spy_rating, "\nOnline: ", spy_online;
        spy['name'] = spy_name;
        spy['age'] = spy_age;
        spy['rating'] = spy_rating;
        spy['is_online'] = spy_online;
        start_chat(spy);
    else:
        print ""+error
elif (existing == 'Y' or existing == 'y'):
    print "Okay lets get started"
    print "Authentication complete. Welcome " + spy['name'] + "\n" + "age: ", spy['age'], "\nRating: ", spy['rating'], "\nOnline: ", spy['is_online'];
    start_chat(spy);
else:
    print "Wrong input";