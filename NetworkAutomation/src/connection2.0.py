import paramiko, os, sys, time, schedule, colorama, getpass
from termcolor import colored

colorama.init()

def connection():

    print("--CONNECTION HAS STARTED--")

    username = input("Username: ")
    password = getpass.getpass("Password: ")

    try:

        file = open('../data/addresses.txt', 'r')
        hostnames = []
        for line in file:
            hostnames.append(line.strip())

        file.close()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('200.204.1.4', port=22, username=username, password=password)

        print(colored("--CONNECTED TO JUMPER--", "yellow"))

        for hostname in hostnames:

            cmds = ['ssh ' + hostname, 'terminal length 0', 'show ip bgp summary vrf all | i 10429', 'terminal length 30' ]

            #vrfs = ["AWS_INPOST", "AWS_OUTPOST", "BILHETAGEM-S", "CONTACT_CENTER", "CONTROL_UNICA", "DATA_UDC_AMBAPA", "DATA_UDC_PRSCRS", "DMZ", "DNS_IES", "DNS_NOMINUM", "GERENCIA_CS", "GERENCIA_NGN", "GER_ACESSO_FIXO", "GER_PS", "GLOBAL", "GN", "HRS_INTERNAL", "INTERCONEXAO_SIP_11_H", "INTERCONEXAO_SIP_21_H", "INTERCONEXAO_SIP_31_H", "INTERCONEXAO_SIP_41_H", "INTERCONEXAO_SIP_48_H", "INTERCONEXAO_SIP_92_H", "IPTV_OPEN_UCAST", "MOBILE_CONTROL", "MP-BGP", "MP-BGP ", "MVNO", "OPER", "OVERLAY_UNICA", "PROV_UDC_AMBAPA", "PROV_UDC_PRSCRS", "REDE_MGMT", "REPLICATION", "REPLICATION_DB_BROKER", "SINALIZACAO", "SINALIZACAO_V3_V1", "SINALIZACAO_V3_V2", "SYNC_UNICA", "VOIP_RES_PARES_H", "VOZ", "VOZ_V3_V1", "VOZ_V3_V2", "VRF_DEA_DMZ"]

            '''for vrf in vrfs:
                cmds.append("show ip bgp summary vrf " + vrf + " | i 10429")'''
            
            print(colored(len(cmds), "red"))
            channel = client.invoke_shell()

            channel_data = ""

            for cmd in cmds:
                time.sleep(1)
                if channel.recv_ready():
                    channel_data += channel.recv(99999999).decode()
                channel.send(cmd)
                channel.send('\n')
                time.sleep(5)
                if cmd == 'ssh ' + hostname:
                    channel.send(password)
                    channel.send("\n")
                time.sleep(2)
                print(cmd)
            
            if channel.recv_ready():
                channel_data += channel.recv(99999999).decode()
            
            f = open('../data/data.txt', 'a')
            f.write("\n------NEW CONNECTION TO " + hostname + "------\n")
            f.write(channel_data)

            message = "GOT DATA FROM CONNECTION TO " + hostname
            print(colored(message, "blue"))
            
            f.close()
            channel.close()
            
        client.close()

    except Exception as e:
        print("Program couldn't start or proceed")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
        print(exc_type, exc_tb.tb_lineno)

schedule.every(5).seconds.do(connection)

while True:
    schedule.run_pending()
    time.sleep(1)