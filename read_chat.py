from select_friend import select_friend
from spy_details import friend_list
from spy_details_class import Spy_Details
from colorama import init,Fore

sd = Spy_Details()
init()


def read_chat():
    choice=select_friend()
    if choice == "error":
        print Fore.RED+"Wrong choice"+Fore.RESET
    else:
        print (Fore.GREEN + "Messages sent by you is shown in green color \n" + Fore.RED + "Messages received and read by your friend is shown in red color:")
        choice=int(choice)
        chats=friend_list[choice].get_chats()
        for chat in chats:
            if chat['send_by_me']:
                print (Fore.BLUE + str(chat['time']) + " " + Fore.GREEN + sd.get_name() + " " + Fore.RESET + chat['message'])
            else:
                print (Fore.BLUE + str(chat['time']) + " " + Fore.RED + friend_list[choice].get_name() + " " + Fore.RESET + chat['message'])
