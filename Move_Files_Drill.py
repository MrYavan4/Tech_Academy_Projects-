# Python Version:       2.7.12
#
# Author:               Tanvir Khondakar
#
# Purpose:              Creating a function that will figure out if a files was updated within the last
#                       24 hours so it can be transfered to another folder. 


# Import necessary libraries
import os
import datetime
import shutil

# Set the path

org_path = 'C:/Users/tanvir/Desktop/Folder_A'
dst_path = 'C:/Users/tanvir/Desktop/Folder_B'


# Loop through the files to process 

def file_transfer():
    
    # Loop through the files to find out when they were last updated.
    for root, dirs, files in os.walk(org_path):
        for filename in files:
            filename = os.path.join(root, filename)

            # Get today's date
            today_date = datetime.date.today()

            # Get dates for new and modded files
            new_file = (datetime.date.fromtimestamp(os.stat(filename).st_ctime))
            mod_file = (datetime.date.fromtimestamp(os.stat(filename).st_mtime))

            if mod_file == today_date or new_file == today_date:
                shutil.move(filename, dst_path)
                print('Files Transfered')
            else:
                print('No files to update today')

# Run function
file_transfer()
