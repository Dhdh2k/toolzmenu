import colorama
from colorama import Fore, Back, Style
colorama.init()
from colorama import init, Fore
import os
import time

print("loading toolzy...")
time.sleep(1)





def print_logo():
  logo = """     ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄    ▄▄▄        ▄▄▄▄▄▄▄    ▄▄   ▄▄
█████████  █████████  █████████  █████      █████████  ████ ████
█████████  █████████  █████████  █████      █████████  ████▄████
  █████    ████ ████  ████ ████  █████       ▄▄▄▄████  █████████
  █████    ████▄████  ████▄████  █████▄▄▄   █████████  █████████
  █████    █████████  █████████  █████████  ███▄▄▄▄▄     █████
  █████    █████████  █████████  █████████  █████████    █████   """
  print(logo)
print_logo()
time.sleep(3)


print (Fore.BLUE + '\n[+[+[+[ TOOLZY v1.0 ]+]+]+]\n')
time.sleep(2)



def print_logo():
  logo = """ ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⡀
⢻⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⢠⣾⡇
⢸⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⢤⣶⠶⠶⢶⣶⡤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢀⣴⠋⢀⠇
⠈⣇⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠋⢉⡴⠞⠋⣿⠀⠀⠀⡯⠙⠳⣦⡉⠙⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⣼⠀
⠀⠹⣆⠀⠀⠈⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠀⢀⣰⠏⠀⠀⠀⢻⡄⠀⢰⠇⠀⠀⠈⢻⣄⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠁⠀⠀⣰⠃⠀
⠀⠀⠹⣇⠀⠀⠀⠀⠉⠳⢦⣄⡀⠀⠀⠀⢀⡾⠃⠀⣠⠞⠋⠁⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠉⠙⢷⣄⠀⠙⢧⡀⠀⠀⠀⢀⣠⡶⠛⠁⠀⠀⠀⠀⣴⠃⠀⠀
⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠈⠙⠳⠶⢤⣿⣄⣀⣸⠋⢠ by dhdh2k24     ⢠⠀⢹⣆⣀⣨⣷⡤⠶⠚⠋⠁    ⠀⢠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠈⡇⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣼⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣧⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⡟⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣦⣀⠀⠀⠀⠀⠀⠀⢀⡟⠀⡏⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⣿⠀⢿⡀⠀⠀⠀⠀⠀⠀⣠⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡆⠉⢻⡶⢤⣀⡀⢀⡾⠁⣼⠃⠀⠀⠀⠀⠀⠀⣸⠹⣆⠀⠀⠀⠀⠀⠀⠹⣆⠘⢧⡀⢀⣠⡤⢶⡟⠉⢰⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⣧⠀⢸⠃⠀⣨⠿⠋⣠⠞⠁⠀⠀⠀⠀⠀⠀⢸⡏⠀⣹⡆⠀⠀⠀⠀⠀⠀⠘⢦⣈⠛⢿⡅⠀⢸⡇⠀⡿⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡕⣿⣧⣸⡀⠀⠛⡶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⣾⠃⠀⢸⣇⡼⡿⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠘⢯⡙⠷⣄⣸⠇⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠹⣄⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⢹⣆⣠⠞⣫⡿⠁⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⢀⠙⢷⡘⣿⣷⡶⣄⠙⠷⣄⡀⠀⠀⠀⠘⠁⠀⠀⠀⠈⠃⠀⠀⠀⢀⣴⠞⢁⣤⢶⣾⡿⢡⡾⠋⡀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⠀⠸⣇⠈⣻⣷⣿⠳⣤⡈⠙⠓⠄⠀⠈⠳⡄⠀⣰⠛⠁⠀⠠⠞⠋⢀⣴⠟⣇⣿⡟⠀⣾⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠻⣾⠏⠸⣿⣦⡈⠛⠶⢤⣤⣤⣤⠴⡷⠶⣿⠦⣤⣤⣤⡤⠾⠋⢁⣼⣿⠁⠹⣶⠏⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣄⠀⣿⠀⠀⠘⠿⣿⣦⣤⢴⣿⡿⠃⠀⡷⠛⣦⠀⠘⢿⣷⠦⣤⣶⣿⠟⠁⠀⢀⡿⢀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠘⣷⣄⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⡇⠀⡟⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⣠⣾⠁⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣴⡏⢹⢷⣦⣄⡀⠀⣀⣤⡤⢤⡀⡧⠀⠇⢀⡤⢤⣤⡀⠀⣀⣠⣴⣿⡏⢻⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠈⣧⢸⡾⠁⣨⣿⡟⠙⢯⣀⠀⠀⠀⠀⠀⠀⢀⣀⡿⠉⢻⢿⡁⠘⣿⠃⡿⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡓⠶⠶⠿⡛⠥⠞⠉⢠⣿⣄⡀⠉⠉⠻⣦⣀⡴⠛⠉⠉⢀⣴⣿⡀⠙⠲⠬⣻⠷⠶⠶⢚⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣄⣀⣀⣀⣠⣴⡋⢻⣿⡛⢳⠒⣤⠼⣿⠧⣤⢲⡞⢻⣿⠋⢹⡦⣄⣀⣀⣀⣤⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣆⠈⠛⣾⣿⣧⣿⠙⠛⠓⠛⠚⠛⢋⣇⡾⣿⣷⠋⠀⣼⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⣿⣿⣆⠙⠃⠀⠀⠀⠀⠀⠘⠋⣼⡿⣿⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡿⣮⡙⠛⣟⣻⣯⣯⣽⣟⣿⠛⢋⣴⣷⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣼⣏⠛⣋⣤⠶⠒⠶⣤⣙⠛⣹⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡉⠉⠉⠀⣠⣤⡄⠀⠉⠉⢁⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠲⠤⠞⠋⠀⠙⠶⠤⠖⠋⠁ """
  print(logo)
print_logo()

time.sleep(3)
print (Fore.BLUE + '\n[+[+[+[ careful who you trust segeant ]+]+]+]\n')
time.sleep(2)
print (Fore.MAGENTA + '\n[+[+[+[ people you know can hurt you the most ]+]+]+]\n')
time.sleep(2)


def print_logo():
  logo = """   _              _      _  _                               
| |_  ___  ___ | | ___| || |       _ __   ___  _ _   _  _ 
|  _|/ _ \/ _ \| ||_ / \_. |      | '  \ / -_)| ' \ | || |
 \__|\___/\___/|_|/__| |__/       |_|_|_|\___||_||_| \_._|   """
  print(logo)
print_logo()
time.sleep(2)


init(autoreset=True)

def print_red(text):
    """Prints text in red color."""
    print(Fore.RED + text)

def show_menu():
    """Displays a simple menu with red text."""
    print_red("[1] DARKARMY                       [2] Virus-X                  [3] pin brute force")
    print_red("[4] ghost_eye                      [5] virus builder            [6] infect")
    print_red("[7] ducky virus                    [8] DDoS ripper              [9] cam phish")
    print_red("[10] ip drone                      [11] ig hack                 [12] hack lock")
    print_red("[13] grabcam                       [14] camhackers              [15] userrecon")
    print_red("[16] zphisher                      [17] unfollow plus           [18] hacking tool")
    print_red("[19] aliens_eye                    [20] TeletraX                [21] tiktok fame") 
    print_red("[22] anon sms                      [23] 48 laws of power        [24] free anime")
    print_red("[25] free movies                   [26] rent a phone number     [27] dark web chat-room links")
    print_red("[28] vpn ")
    



    

def main():
    while True:
        show_menu()
        choice = input(Fore.BLUE + "Enter your choice: ")

        if choice == '1':
            print_red("You selected darkarmy.")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/D4RK-4RMY/DARKARMY.git")
            os.system("cd DARKARMY")
            os.system("chmod +x install.sh")
            os.system("./install.sh")
            os.system("DARKARMY")
            break




        elif choice == '2':
            print_red("You selected virus-x.")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/TSMaitry/VirusX.git")
            os.system("cd VirusX")
            os.system("chmod +x VirusX.py")
            os.system(" python2 VirusX.py")
            break





        elif choice == '3':
            print_red("You selected pin brute force.")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/HAKDAD/an_pinbruter")
            os.system("cd an_pinbruter")
            os.system("bash Pinbruter.sh")
            break




        elif choice == '4':
            print_red("You selected ghost_eye")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/BullsEye0/ghost_eye.git")
            os.system("cd ghost_eye")
            os.system("pip3 install -r requirements.txt")
            os.system("python3 ghost_eye.py")
            break


            
        elif choice == '5':
            print_red("You selected virus builder")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/Cyber-Dioxide/Virus-Builder/")
            os.system("cd Virus-Builder")
            os.system("pip install -r requirements.txt")
            os.system("python3 Builder.py")
            break




        elif choice == '6':
            print_red("You selected infect")
            print_red("loading...")
            os.system("pip install lolcat")
            os.system("git clone https://github.com/noob-hackers/infect")
            os.system("cd infect")
            os.system("bash infect.sh")
            break



        elif choice == '7':
            print_red("You selected ducky virus.")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/hackerxphantom/HXP-DUCKY")
            os.system("cd HXP-DUCKY")
            os.system("bash hxp_ducky.sh")
            break

    





        elif choice == '8':
            print_red("you entered ddos ripper")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/palahsu/DDoS-Ripper.git")
            os.system("cd DDoS-Ripper")
            os.system("python3 DRipper.py")
            break



        elif choice == '9':
            print_red("you selected cam phish")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/techchipnet/CamPhish")
            os.system("cd CamPhish")
            os.system("bash camphish.sh")
            break



        elif choice == '10':
            print_red("you selected ip drone")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/noob-hackers/ipdrone")
            os.system("cd ipdrone")
            print_red("please type the following command")
            time.sleep(2)
            print_red("python ipdrone.py -v (your victim ip here)")
            break




        elif choice == '11':
            print_red("you selected ig hack")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/noob-hackers/ighack")
            os.system("cd ighack")
            os.system("bash setup")
            os.system("bash ighack.sh")
            break



        elif choice == '12':
            print_red("you selected hack lock")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/noob-hackers/hacklock")
            os.system("cd hacklock")
            os.system("bash setup")
            os.system("bash hacklock.sh")
            break



        elif choice == '13':
            print_red("you selected grabcam")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/noob-hackers/grabcam")
            os.system("cd grabcam")
            os.system("bash setup")
            os.system("bash grabcam.sh")
            break


        elif choice == '14':
            print_red("you selected cam-hackers")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
            os.system("cd Cam-Hackers")
            os.system("pip install -r requirements.txt")
            os.system("python3 cam-hackers.py")
            break



        elif choice == '15':
            print_red("you selected userrecon")
            print_red("loading....")
            time.sleep(4)
            os.system("git clone https://github.com/wishihab/userrecon.git")
            os.system("cd userrecon")
            os.system(" ./userrecon.sh")
            break



        elif choice == '16':
            print_red("you selected zphisher")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")
            os.system("cd zphisher")
            os.system("bash zphisher.sh")
            break



        elif choice == '17':
            print_red("you selected unfollow plus")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/htr-tech/unfollow-plus")
            os.system("cd unfollow-plus")
            os.system("bash unfollower.sh")
            break



        elif choice == '18':
            print_red("you selected hacking tool")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/Z4nzu/hackingtool.git")
            os.system("chmod -R 755 hackingtool")
            os.system("cd hackingtool")
            os.system("sudo bash install.sh")
            os.system("sudo hackingtool")
            break



        elif choice == '19':
            print_red("you selected aliens_eye")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/Z4nzu/hackingtool.git")
            os.system("cd Aliens_eye")
            os.system("bash install.sh")
            print_red("please type the following command")
            time.sleep(3)
            print_red("aliens_eye <USERNAME>")
            break




        elif choice == '20':
            print_red("you selected TeletraX")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/MrHacker-X/TeletraX.git")
            os.system("cd TeletraX")
            os.system("bash setup.sh")
            os.system("python teletrax.py")
            break



        elif choice == '21':
            print_red("you selected Tiktok fame")
            print_red("loaading...")
            time.sleep(4)
            print(Fore.GREEN + "please search the following link for your tiktok bots")
            print(Fore.LIGHTBLUE_EX + "https://zefoy.com")
            break



        elif choice == '22':
            print_red("you selected anon sms")
            print_red("loading...")
            time.sleep(4)
            os.system("git clone https://github.com/HACK3RY2J/Anon-SMS.git")
            os.system("cd Anon-SMS")
            os.system("sudo bash Run.sh")
            break
            




        elif choice == '23':
            print_red("you selected 48 laws of power")
            print_red("\n\n\n\n\n\n\n\nloading...")
            time.sleep(2)
            print_red("\n\n\n\n\nlaw 1")
            time.sleep(2)
            print(Fore.BLUE + "never outshine the master")
            time.sleep(3)
            print_red("\nlaw 2")
            time.sleep(2)
            print (Fore.BLUE + "never put too much trust in friends, learn how to use enimies")
            time.sleep(2)
            print_red("\nlaw 3")
            time.sleep(2)
            print(Fore.BLUE + "conceal your intentions")
            time.sleep(2)
            print_red("\nlaw 4")
            time.sleep(2)
            print(Fore.BLUE + "always say less than necessary")
            time.sleep(3)
            print_red("\nlaw 5")
            time.sleep(2)
            print(Fore.BLUE + "so much repuation--gaurd it with your life")
            time.sleep(2)
            print_red("\nlaw 6")
            time.sleep(2)
            print(Fore.BLUE + "court attention at all cost")
            time.sleep(3)
            print_red("\nlaw 7")
            time.sleep(2)
            print(Fore.BLUE + "get others to do the work for you, but always take the credit")
            time.sleep(3)
            print_red("\nlaw 8 ")
            time.sleep(2)
            print (Fore.BLUE + "make other people to come to you, use bait if necessary")
            time.sleep(3)
            print_red("\nlaw 9")
            time.sleep(2)
            print (Fore.BLUE + "win through your actions, never through argument")
            time.sleep(3)
            print_red("\nlaw 10")
            time.sleep(2)
            print(Fore.BLUE + "infecion: avoid the unlucky")
            time.sleep(3)
            print_red("\nlaw 11")
            time.sleep(2)
            print(Fore.BLUE + "learn to keep people dependent on you")
            time.sleep(3)
            print_red("\nlaw 12")
            time.sleep(2)
            print (Fore.BLUE + "use selective honestly and generosity to disarm your victim")
            time.sleep(3)
            print_red("\nlaw 13")
            time.sleep(2)
            print(Fore.BLUE + "when asking for help, appeal to peoples self intrest, never to their mercy or gratitude")
            time.sleep(4)
            print_red("\nlaw 14")
            time.sleep(2)
            print(Fore.BLUE + "pose as a friend, work as a spy")
            time.sleep(3)
            print_red("\nlaw 15")
            time.sleep(2)
            print(Fore.BLUE + "crush your enemy totally")
            time.sleep(2)
            print_red("\nlaw 16")
            time.sleep(2)
            print(Fore.BLUE + "use absence to increase respect and honor")
            time.sleep(2)
            print_red("\nlaw 17")
            time.sleep(2)
            print(Fore.BLUE + "keep others in suspended terror: cultivate an air of unpredictability")
            time.sleep(3)
            print_red("\nlaw 18")
            time.sleep(2)
            print(Fore.BLUE + "do NOT build fortresses to protect yourself, isolation is dangerous")
            time.sleep(3)
            print_red("\nlaw 19")
            time.sleep(2)
            print(Fore.BLUE + "know who your dealing with, do not offend the wrong person")
            time.sleep(3)
            print_red("\nlaw 20")
            print(Fore.BLUE + "do not commit to anyone")
            time.sleep(3)
            print_red("\nlaw 21")
            time.sleep(2)
            print(Fore.BLUE + "play a sucker to catch a sucker, seem dumber than your mark")
            time.sleep(3)
            print_red("\nlaw 22")
            time.sleep(2)
            print(Fore.BLUE + "use the surrender tatic: transform weakness into power")
            time.sleep(3)
            print_red("\nlaw 23")
            time.sleep(2)
            print(Fore.BLUE + "conentrate your forces")
            time.sleep(3)
            print_red("\nlaw 24")
            time.sleep(2)
            print(Fore.BLUE + "play the perfect courtier")
            time.sleep(3)
            print_red("\nlaw 25")
            time.sleep(2)
            print(Fore.BLUE + "re-create yourself")
            time.sleep(3)
            print_red("\nlaw 26")
            time.sleep(2)
            print(Fore.BLUE + "keep your hands clean")
            time.sleep(3)
            print_red("\nlaw 27")
            time.sleep(2)
            print(Fore.BLUE + "play on peoples need to belive to create a cultlike following")
            time.sleep(3)
            print_red("\nlaw 28")
            time.sleep(2)
            print_red(Fore.BLUE + "enter actions with boldness")
            time.sleep(3)
            print_red("\nlaw 29")
            time.sleep(2)
            print(Fore.BLUE + "plan all the way to the end")
            time.sleep(3)
            print_red("\nlaw 30")
            time.sleep(2)
            print(Fore.BLUE + "make your accomplishments seem efforts")
            time.sleep(3)
            print_red("\nlaw 31")
            print(Fore.BLUE + "control the options: get others to play with the cards you deal")
            time.sleep(3)
            print_red("\nlaw 32")
            time.sleep(2)
            print(Fore.BLUE + "play to peoples fantasies")
            time.sleep(3)
            print_red("\nlaw 33")
            time.sleep(2)
            print(Fore.BLUE + "discover each mans thumbscrew(weakness)")
            time.sleep(3)
            print_red("\nlaw 34")
            time.sleep(2)
            print(Fore.BLUE + "be royal in your own fashion, act like a king to be treated like one")
            time.sleep(3)
            print_red("\nlaw 35")
            time.sleep(2)
            print(Fore.BLUE + "master the art of timing")
            print_red("\nlaw 36")
            time.sleep(2)
            print(Fore.BLUE + "disdain things you cannot have, ignoring them is the best revenge")
            time.sleep(3)
            print_red("\nlaw 37")
            time.sleep(2)
            print(Fore.BLUE + "create compelling spectacles")
            time.sleep(3)
            print_red("\nlaw 38")
            time.sleep(2)
            print(Fore.BLUE + "think as you like but behave like others")
            time.sleep(3)
            print_red("\nlaw 39")
            time.sleep(2)
            print(Fore.BLUE + "stir up waters to catch fish")
            time.sleep(3)
            print_red("\nlaw 40")
            time.sleep(2)
            print(Fore.BLUE + "despair the free lunch")
            time.sleep(3)
            print_red("\nlaw 41")
            time.sleep(2)
            print(Fore.BLUE + "avoid stepping into a great mans shoes")
            time.sleep(3)
            print_red("\nlaw 42")
            time.sleep(2)
            print(Fore.BLUE + "strike the sheep and the sheep will scatter")
            time.sleep(3)
            print_red("\nlaw 43")
            time.sleep(2)
            print(Fore.BLUE + "work on the hearts and minds of people")
            time.sleep(3)
            print_red("\nlaw 44")
            time.sleep(2)
            print(Fore.BLUE + "disarm and infuriate with the mirror effect")
            time.sleep(3)
            break






        elif choice == '24':
            print_red("you chose free anime")
            time.sleep(2)
            print (Fore.CYAN + "please visit the following link to watch free anime")
            time.sleep(2)
            print(Fore.BLUE + "http://zorox.to")
            break




        elif choice == '25':
            print_red("you chose free movies")
            time.sleep(2)
            print(Fore.CYAN + "please visit the following website to watch free movies")
            time.sleep(2)
            print(Fore.LIGHTCYAN_EX + "hdtoday.cc")
            break



        elif choice == '26':
            print("you chose to rent a phone number")
            print("loading...")
            time.sleep(2)
            print(Fore.BLUE + "please visit the following link to rent a phone number")
            time.sleep(3)
            print(Fore.GREEN + "https://sms-man.com")
            break



        elif choice =='27':
         print_red("you selected dark web chat rooms links")
         time.sleep(2)
         print("loading...") 
         time.sleep(2)
         print(Fore.BLUE + "Black Hat Chat - http://blkhatjxlrvc5aevqzz5t6kxldayog6jlx5h7glnu44euzongl4fh5ad.onion/")
         time.sleep(1)
         print(Fore.GREEN + "MEGA Tor Chat - http://ylmjp76zk4ndvgpncbtgzrfsrzpblvlzgtuoduqgygwdlexou64iwfqd.onion/")
         time.sleep(1)
         print(Fore.BLUE + "El Chat de Eliza -  http://intor3nu3dvbsxr2iyzmyfsjnr3mt6fv3a7gt7ji6pnycxc4rpiet3qd.onion/")
         time.sleep(1)
         print(Fore.GREEN + "Endchan - http://enxx3byspwsdo446jujc52ucy2pf5urdbhqw3kbsfhlfjwmbpj5smdad.onion/")
         time.sleep(1)
         print_red("\n\n\n\nThe following addresses are V2 only (they don't have V3 addresses yet)")
         time.sleep(2)
         print(Fore.BLUE + "http://tetatl6umgbmtv27.onion – Talk to John Doe!, Randomized, anonymous chat.")
         time.sleep(1)
         print(Fore.GREEN + "http://kaarvixjxfdy2wv2.onion – Wizardry, Loads of docs mostly pertaining to computers.")
         time.sleep(1)
         print(Fore.BLUE + "http://q2uftrjiuegl4ped.onion – TorDuckin, create a new account and chat til you drop")
         time.sleep(1)
         print(Fore.GREEN + "http://chatrapi7fkbzczr.onion – OnionChat,  Minimalist chat interface. No JS required.")
         time.sleep(1)
         print(Fore.BLUE + "http://kitsune6uv4h3dve.onion – kitsune, Volatile’s chat. Chat on irc or via jabber.")
         time.sleep(1)
         print(Fore.GREEN + "http://chattorci7bcgygp.onion – ChatTor A new, chat site. Select a nick and hit “enter”")
         time.sleep(1)
         print(Fore.BLUE + "http://tt3j2x4k5ycaa5zt.onion – Daniel, chat among Daniel’s clients until you puke")
         time.sleep(1)
         print(Fore.GREEN + "http://torbitamzta34aai.onion – TorBit, old school BBS. Connect via ssh to chat and message.")
         time.sleep(1)
         print(Fore.BLUE + "http://vrimutd6so6a565x.onion – Dark Lair Garnech the Prime’s site. Message")
         time.sleep(1)
         break



        elif choice == '28':
            print(Fore.BLUE +"you selected vpn")
            time.sleep(2)
            print("loading...")
            time.sleep(3)
            print_red("cyber ghost")
            time.sleep(1)
            print(Fore.BLUE + "https://www.cyberghostvpn.com/")
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX + "privateinternetaccess")
            time.sleep(1)
            print(Fore.CYAN + "privateinternetaccess.com")
            print_red("ipvanish")
            time.sleep(1)
            print(Fore.CYAN + "ipvanish.com")
            time.sleep(1)
            print_red("privatevpn")
            time.sleep(1)
            print(Fore.GREEN + "privatevpn.com")
            time.sleep(1)
            print_red("nordvpn")
            time.sleep(1)
            print(Fore.GREEN + "nordvpn.com")
            time.sleep(1)
            print_red("surfshark")
            time.sleep(1)
            print(Fore.GREEN + "surfshark.com")
            time.sleep(2)
            break
        















      
      
      
        elif choice == 'e':
            print_red("thank you for using this program goodbye")
            break

        else:
            print_red("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

