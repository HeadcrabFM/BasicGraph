from colorama import Fore, Back, Style
import simple1 as s1
import weight as w

def mainmenu():

    print(Fore.YELLOW + "# # # # # # # # # # # # # # # # \n"
                      "# # # WELCOME 2 MAIN MENU # # #\n"
                      "# # # # # # # # # # # # # # # # \n")
    a=int(input(Fore.BLUE + "Введите номер главы:\n"
                            "1. y^3\n"
                            "2. вес\n"
                            "0. exit\n\n"
                            ">>> "))
    if a==1:
        s1.Simple1()
    elif (a==2):
        w.Weight()

    elif (a==0):
        print(Fore.RED + "Exit")
        exit()
    else:
        print(Fore.RED + "ERROR")
