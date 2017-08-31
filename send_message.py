from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime;
from spy_details import friend_list;
def send_message():
    #TODO function Logic
    friend_choice = select_friend();
    time=datetime.now();
    print (type(time));
    type(time);
    if (friend_choice == "error"):
        print "wrong choice"
    else:
        friend_choice = int(friend_choice);
        print friend_choice;
        original_image=raw_input("Provide name of image to hide message into")
        output_image= raw_input("Provide the name of output image")
        text=raw_input("Enter your message")
        Steganography.encode(original_image,output_image,text);

        print "Message encrypted successfully"

    #Save the chats
    new_chat={
        'message':text,
        'time':datetime.now(),
        'send_by_me':True
    }

    #saving the dictionary
    friend_list[friend_choice]['chats'].append(new_chat)
    print "Message saved"
