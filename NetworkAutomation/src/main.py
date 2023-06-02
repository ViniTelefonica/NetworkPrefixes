#start_all
import os

try:
    with open("install/package_installation.py") as f:
        exec(f.read())

    from termcolor import colored
    import colorama

    colorama.init()
    print(colored("PACKAGES WERE SUCCESFULLY INSTALLED!", "yellow"))

    with open("./connection2.0.py") as prog:
        exec(prog.read())

except Exception as e:
    print (e)




