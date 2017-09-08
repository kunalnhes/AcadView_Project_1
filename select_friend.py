from spy_details import friend_list
def select_friend():
    i=1
    for friend in friend_list:
        print str(i)+" Name : "+friend.get_name()+ "  Age : " + str(friend.get_age())
        i=i+1;
    result = int(raw_input("Select your friend from the list: "))
    if(result>0 and result<i):
        return result-1
    else:
        return "error"
