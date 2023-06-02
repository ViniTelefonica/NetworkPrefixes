import paramiko, os, sys, time, schedule, colorama
from termcolor import colored

colorama.init()

def connection():
    hostnames_txt = open("../data/addresses.txt", "r")
    hostnames = []
    for line in hostnames_txt:
        hostnames.append(line.strip())

    port = 22 
    username = '40416438' 
    password = '@K0a5t0h4e@'

    try:
        for hostname in hostnames:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, port=port, username=username, password=password)

            channel = client.invoke_shell()
            channel_data = ""

            cmds = ["whoami"]
            ##loopbacks = list_of_loopbacks()

            for cmd in cmds:
                time.sleep(1)
                if channel.recv_ready():
                    channel_data += channel.recv(9999).decode()
                channel.send(cmd)
                channel.send('\n')

            time.sleep(1)
            if channel.recv_ready():
                channel_data += channel.recv(9999).decode()

            f = open('../data/data.txt', 'a')
            f.write("\n------NEW CONNECTION TO " + hostname + "------\n")
            f.write(channel_data)
            
            f.close()
            channel.close()
            client.close()
            message = "GOT DATA FROM CONNECTION TO " + hostname
            print(colored(message, "blue"))

        return channel_data

    except Exception as e:
        print("Program couldn't start or proceed")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
        print(exc_type, exc_tb.tb_lineno)
    
schedule.every(1).seconds.do(connection)

while True:
    schedule.run_pending()
    time.sleep(1)

