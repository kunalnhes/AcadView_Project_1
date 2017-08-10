from spy_details import friends;
friend_list=[];
def add_friends():
    error="";
    new_name = raw_input("Please enetr your friends name:")
    if len(new_name)<=0 :
        error="Name not entered";
    new_salutation = raw_input("How do you want to address your friend")
    if len(new_salutation)<=0:
        error="Salutation not added";
    new_name = new_salutation+" "+new_name;
    new_age = int(raw_input("Please enter the age:"))
    if new_age<15 or new_age>50:
        error = "Age not supported";
    new_rating = raw_input("Please provide the rating of your friend")
    if len(new_rating)<=0:
        error = "Rating not provided"
    if(len(error)<=0):
        print "Friend added to the list"
        friends['name']=new_name;
        friends['age']=new_age;
        friends['rating']=new_rating;
        friends['is_online']=True;
        friend_list.append(friends);
    else:
        print "Not added. Error occured: "+ error;
