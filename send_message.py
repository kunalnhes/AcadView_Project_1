from select_friend import select_friend
from steganography.steganography import Steganography
def send_message():
    #TODO function Logic
    x = select_friend();
    if (x == "error"):
        print "wrong choice"
    else:
        x = int(x);
        print x;
        original_image=raw_input("Provide name of image to hide message into")
        output_image= raw_input("Provide the name of output image")
        text=raw_input("Enter yoyr message")
        Steganography.encode(original_image,output_image,text);