from steganography.steganography import Steganography
from select_friend import select_friend
def read_message():
    #chooose friend from the list
    sendr=select_friend()
    encrypted_image=raw_input("Provide encrypted image: ")
    secret_message=Steganography.decode(encrypted_image)
    print secret_message