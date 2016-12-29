print("Author:Pedro Paulo Andrade")
print("I am not responsible for the misuse of this software")
print("This software is directed to use only of pentesters or for didactic purposes")
print("")
print("")
print("Enter '1' for yes, and '2' for no")
term_use =int(input("Do you accept the terms of use of this program?"))
print("")
print("")
if(term_use == 1):
    print("1-Find ip by sending site link")
    print("2-Create Qrcode")
    print("3-Exploit DataBase")
    print("4-Metasploit Download")
    print("5-Best Linux for pentest")
    print("6-Bests hack programs for Windows")
    print("7-How to use Sqlmap")
    print("8-Comment my project")
else:
    if(term_use == 2):
        print("So you can not use this program")
    else:
        print("Invalid option")
options =int(input("Select an option: "))
if(options == 1):
    print("")
    print("This option, available on this site:")
    print("grabify.link/")
    print("thanks for use")
else:
    if(options == 2):
        print("")
        print("This option, available on this site:")
        print("http://br.qr-code-generator.com/")
        print("thanks for use")
    else:
        if(options == 3):
            print("")
            print("This option, available on this site:")
            print("https://www.exploit-db.com/")
            print("thanks for use")
        else:
            if(options == 4):
                print("")
                print("This option, available on this site:")
                print("https://www.metasploit.com/")
                print("thanks for use")
            else:
                if(options == 5):
                    print("")
                    print("This option, available on this site:")
                    print("https://www.linux.com/news/best-linux-distros-2016")
                    print("thanks for use")
                else:
                    if(options == 6):
                        print("")
                        print("This option, available on this site:")
                        print("https://fossbytes.com/best-hacking-tools-of-2016-windows-linux-mac-osx/")
                        print("thanks for use")
                    else:
                        if(options == 7):
                            print("")
                            print("This option, available on this site:")
                            print("http://www.binarytides.com/sqlmap-hacking-tutorial/")
                            print("thanks for use")
                        else:
                            if(options == 8):
                                print("")
                                print("Give me constructive criticism so I can improve my software.")
                                print("Thank you for your cooperation.")
print("")
print("")
print("Bye")