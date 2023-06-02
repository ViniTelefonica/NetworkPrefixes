import paramiko, os, sys, time, schedule, colorama
from termcolor import colored

colorama.init()

def connection():
    hostnames = ['192.168.3.64', '192.168.3.5'] 
    port = 2222 
    username = 'vini' 
    password = 'vini'

    for hostname in hostnames:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password, allow_agent=False)

        channel = client.invoke_shell()
        channel_data = ""

        cmds = ["whoami", "id", "df -h"]
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
        f.write("------NEW CONNECTION TO " + hostname + "------")
        f.write(channel_data)
        
        f.close()
        channel.close()
        client.close()
        print(colored("GOT STATUS FROM CONNECTION", "blue"))

    return channel_data
    
schedule.every(1).seconds.do(connection)

while True:
    schedule.run_pending()
    time.sleep(1)
