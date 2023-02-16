#Week 13 project
#2-14-2023

#!/usr/bin/env python3.7



import os

# Get the current working directory
my_dir = os.getcwd()

# Create an empty list to store file information
files_list = []

# Loop over the entries in the directory
for entry in os.scandir(my_dir):
    # Get the file path, file name, and size
    file_path = entry.path
    file_name = entry.name
    file_size = entry.stat().st_size
    
    # Create a dictionary with the file information
    file_info = {'path': file_path, 'file_name': file_name, 'size': file_size}
    
    # Append the dictionary to the list of files
    files_list.append(file_info)
    
# Print the list of files
print(*files_list, sep="\n")


    
    print(*files_list, sep="\n")



    
    
    


