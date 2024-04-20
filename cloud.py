
from ftplib import FTP

def upload_file_to_drivehq(file_path, username, password, remote_directory):
    with FTP('ftp.drivehq.com') as ftp:
        ftp.login(username, password)
        ftp.cwd(remote_directory)
        with open(file_path, 'rb') as file:
            ftp.storbinary(f'STOR {file_path.split("/")[-1]}', file)


# from ftplib import FTP

# # Connect to FTP server
# ftp = FTP('')
# ftp.connect('ftp.drivehq.com')
# ftp.login("projectsforu", "1000projects@shan")
# ftp.cwd('/cloud/') #replace with your directory

# # List files in the current directory
# print("Files in directory:")
# ftp.retrlines('LIST')

# # Print current working directory
# print("Current working directory:", ftp.pwd())

# # Function to upload a file
# def uploadFile(filename, path):
#     with open(path, 'rb') as file:
#         ftp.storbinary('STOR ' + filename, file)
#     print("File uploaded successfully.")


# def downloadFile(filename, local_path):
#     with open(local_path, 'wb') as file:
#         ftp.retrbinary('RETR ' + filename, file.write)
#     print("File downloaded successfully.")