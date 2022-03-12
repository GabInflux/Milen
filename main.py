from art import *
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
boucle1 = True

header_final = """
        • ▌ ▄ ·. ▪  ▄▄▌  ▄▄▄ . ▐ ▄ 
        ·██ ▐███▪██ ██•  ▀▄.▀·•█▌▐█
        ▐█ ▌▐▌▐█·▐█·██▪  ▐▀▀▪▄▐█▐▐▌
        ██ ██▌▐█▌▐█▌▐█▌▐▌▐█▄▄▌██▐█▌
        ▀▀  █▪▀▀▀▀▀▀.▀▀▀  ▀▀▀ ▀▀ █▪

V 1.0 - Gab_#8440 - discord.gg/BtNrFc45B7\n\n\n\n"""

while boucle1:
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "[?] Write your text ↓"))
    text_before = input("")
    system('cls')

    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "[?] Write the type of the ascii art you want ↓"))
    ascii_type = input("")
    system('cls')
    
    print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "[?] Do you want to save it in a file (0 = No / 1 = Yes) ↓"))
    try:
        choice = int(input(""))
    except:
        system('cls')
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Please insert a valid number !"))
        sleep(2)
    system('cls')
    
    if choice == 1:
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.cyan_to_blue, "[?] File Name ↓"))
        file_name = input("")
        system('cls')
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
        final_art = text2art(text_before, font=ascii_type)
        tsave(text_before, font=ascii_type, filename=f"{file_name}.txt")
        system('cls')
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
        print(Colorate.Diagonal(Colors.white_to_red, Center.XCenter(final_art)))
        print(Colorate.Diagonal(Colors.cyan_to_blue, "\n\n[?] Press any key to continue"))
        input("")
        system('cls')
        
    else:
        print(Colorate.Diagonal(Colors.cyan_to_blue, Center.XCenter(header_final)))
        final_art = text2art(text_before, font=ascii_type)
        
        print(Colorate.Diagonal(Colors.white_to_red, Center.XCenter(final_art)))
        print(Colorate.Diagonal(Colors.cyan_to_blue, "\n\n[?] Press any key to continue"))
        input("")
        system('cls')