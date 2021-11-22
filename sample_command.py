import pysftp
import sys

myHostname = 'hostname or ip'
myUsername = 'username'
myPassword = 'password'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None # For ignore key

def say_it(var1, var2):
    with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts = cnopts) as sftp:
        sftp.chdir(var1) # change the directory from server side where you want to put the file.
        sftp.put(var2) # upload file from the local machine.

if __name__ == '__main__':
    try:
        var1 = sys.argv[1]
        var2 = sys.argv[2]
        say_it(var1,var2)
    except:
        print("please type the command with arg1 and arg2")

# python .\sample_command.py /root/tmp C:\\Users\\apple\\Desktop\test.txt
