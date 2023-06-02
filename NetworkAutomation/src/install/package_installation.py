import os

paramiko, sys, time, schedule, termcolor, colorama, getpass = "paramiko", "sys", "time", "schedule", "termcolor", "colorama", "getpass"
trig = 0

while trig != 7:
    
    if paramiko != "ok":
        try: 
            import paramiko
            trig += 1
            paramiko = "ok"
        except Exception as e:
            print("Module " + paramiko + " not installed. We are collecting it for you." )
            os.system('py -m pip install paramiko')
            import paramiko
            trig += 0

    if sys != "ok":
        try: 
            import sys
            trig += 1
            sys = "ok"
        except Exception as e:
            print("Module " + sys + " not installed. We are collecting it for you." )
            os.system('py -m pip install sys')
            import sys
            trig += 0

    if time != "ok":
        try: 
            import time
            trig += 1
            time = "ok"
        except Exception as e:
            print("Module " + time + " not installed. We are collecting it for you." )
            os.system('py -m pip install time')
            import time
            trig += 0

    if schedule != "ok":
        try: 
            import schedule
            trig += 1
            schedule = "ok"
        except Exception as e:
            print("Module " + schedule + " not installed. We are collecting it for you." )
            os.system('py -m pip install schedule')
            import schedule
            trig += 0

    if termcolor != "ok":
        try: 
            import termcolor
            trig += 1
            termcolor = "ok"
        except Exception as e:
            print("Module " + termcolor + " not installed. We are collecting it for you." )
            os.system('py -m pip install termcolor')
            import termcolor
            trig += 0

    if colorama != "ok":
        try: 
            import colorama
            trig += 1
            colorama = "ok"
        except Exception as e:
            print("Module " + colorama + " not installed. We are collecting it for you." )
            os.system('py -m pip install colorama')
            import colorama
            trig += 0
    
    if getpass != "ok":
        try: 
            import getpass
            trig += 1
            getpass = "ok"
        except Exception as e:
            print("Module " + getpass + " not installed. We are collecting it for you." )
            os.system('py -m pip install getpass')
            import getpass
            trig += 0









