print "Let's get started"
spy_name = raw_input("Please enter your name: ")
#Concatenation of salutation with the name and condition checking.
if len(spy_name)>0:
    salutation = raw_input("Please enter your salutation: ")

    if len(salutation)>0:
        spy_name = salutation + " " + spy_name
        print "Welcome "+spy_name;
    else:
        print "You did not entered your salutation. Please retry!"

else:
    print "You did not entered your name. Please retry!"