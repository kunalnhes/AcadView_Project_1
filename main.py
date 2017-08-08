print "Let's get started"
spy_name = raw_input("Please enter your name: ")
#Concatenation of salutation with the name and condition checking.
if len(spy_name)>0:
    salutation = raw_input("Please enter your salutation: ")

    if len(salutation)>0:
        spy_name = salutation + " " + spy_name
        print "Welcome "+spy_name;
        print "Okay " + spy_name+ "!! I would like to know more about you "
        spy_age = 0;
        spy_rating = 0.0;
        spy_online = False;

        spy_age = int(raw_input("Enter your age:"));
        print type(spy_age);
        if spy_age>12 and spy_age<50:
            print "you are eligible";
        else:
            print "You are not eligible";
        spy_rating = float(raw_input("Enter your rating:"));
        print type(spy_rating);
        if(spy_rating>=4.5):
            print "Brilliant Spy.";
        elif (spy_rating>=3.5 and spy_rating<4.5):
            print "You are good Spy.";
        elif (spy_rating>=2.5 and spy_rating<3.5):
            print "you can do better."
        else:
            print "You need to work hard.";
        spy_online=True;
        print type(spy_online);
        print "Authentication complete. Welcome "+spy_name+"\n"+"age: ",spy_age,"\nRating: ",spy_rating,"\nOnline: ",spy_online ;
    else:
        print "You did not entered your salutation. Please retry!"

else:
    print "You did not entered your name. Please retry!"
# to print variable we do like:
    # user_name="Kunal Janghel"
    # print "My name is %s" %(user_name);
    #%d for integer
    #%f for float
    #%.2f for flaot with two decimals......