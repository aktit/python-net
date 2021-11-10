import pysftp
myHostname = 'ip address'
myUsername = 'username'
myPassword = 'password'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None # For ignore key`
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts = cnopts) as sftp:
    sftp.cwd('/root') # current working directory

    sftp.cd('/root') # change the directory

    sftp.put('/directory/filename') # upload file to /directory/filename on remote

    sftp.get('remote_file') # get a remote file

    directory_structure = sftp.listdir_attr() # Fetch the content of the directory

    for attr in directory_structure:  # Print the content
        print(attr.filename, attr)

# https://pysftp.readthedocs.io/en/release_0.2.9/
