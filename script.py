from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

# Step 1: Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

# Step 2: Define a function to download a folder
def download_folder(folder_id, destination):
    # Create a directory for the folder to be downloaded
    if not os.path.exists(destination):
        os.makedirs(destination)

    # List all files in the folder
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

    for file in file_list:
        file_path = os.path.join(destination, file['title'])
        if file['mimeType'] == 'application/vnd.google-apps.folder':
            # If the file is a folder, call the function recursively
            download_folder(file['id'], file_path)
        else:
            # If the file is not a folder, download it
            print(f"Downloading {file['title']} to {file_path}")
            file.GetContentFile(file_path)

# Step 3: Specify the folder ID and destination
folder_id = '1CqRSVdn28MO3UzrSlv27ReJOV7v8ChzV'
destination = '.'

# folder_id = 'your_google_drive_folder_id_here'
# destination = 'your_local_folder_path_here'

# Step 4: Download the folder
download_folder(folder_id, destination)
