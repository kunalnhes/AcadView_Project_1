from steganography.steganography import Steganography
from select_friend import select_friend
from spy_details import friend_list
from datetime import datetime
def read_message():
    #chooose friend from the list
    sender=select_friend()
    encrypted_image=raw_input("Provide encrypted image: ")
    secret_message=Steganography.decode(encrypted_image)

    new_chat = {
        'message': secret_message,
        'time': datetime.now(),
        'send_by_me': False
    }

    friend_list[sender]['chats'].append(new_chat)
    print "Message saved"
