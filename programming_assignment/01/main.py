# importing os module
import os

# Get current working directory
current_working_directory = os.getcwd()

# Print current working directory
print(current_working_directory)

# List items in current directory
os.listdir(current_working_directory)

# Print all files on current working directory
# print(os.listdir(current_working_directory))


# 1. We need to find 'mysub' directory from the current working directory first.
# 2. If 'mysub' exists in the current working directory then we can use listdir() function on 'mysub' to list the files in it.
if 'mysub' in os.listdir(current_working_directory):
    content_of_mysub_directory_in_current_directory = os.listdir('mysub')
    # display the contents of only 'mysub' directory available in current directory.
    print(content_of_mysub_directory_in_current_directory)
