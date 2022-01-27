import subprocess
import sys
import time
import traceback

fileShareIP = '10.25.187.31'
fileSharePassword = 'interOP@837-01'
hostName = 'renbdl754837-01.bpc.broadcom.net'
fileShareUserName = 'administrator'
uimVersion = '20.4'
uim_installer_location = r'C:\sw\robot_install'

netusecmd = r"net use \\{}\C$\sw {} /user:{}\{}".format(fileShareIP, fileSharePassword, hostName, fileShareUserName)
a = 'ipconfig'
def archive_pkg_copying():
    """ copying packages from LVFILESHARE.dhcp.broadcom.net to UIM server machine"""
    try:
        # remote_connection().create_service()

        print("copying packages from renbdl754837-01.bpc.broadcom.net to UIM server machine")
        print(netusecmd)
        cmd = subprocess.Popen(['{}'.format(netusecmd)], shell= True, stderr=subprocess.PIPE, universal_newlines=True, stdout=subprocess.PIPE)
        stdout, stderr = cmd.communicate()
        exit_code = cmd.wait()
        print(exit_code)
        if exit_code == 0:
            print('net use command executed successfully : ', stdout)

        else:
            print('Failed to execute net use command :  {}.......\n {} '.format(stderr, stdout))
            print("Exit from the program with above issue...")
            sys.exit(1)
    except Exception as e:
        print('Below exception occured')
        traceback.print_exc()


archive_pkg_copying()