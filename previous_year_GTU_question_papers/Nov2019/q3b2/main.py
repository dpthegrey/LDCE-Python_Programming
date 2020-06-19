# Python program to demonstrate merging of two files
"""
Let the given two files be file1.txt and file2.txt. 
Our Task is to merge both files into third file say file3.txt. 
The following are steps to merge.
1. Create a list containing filenames.
2. Open the file3 in write mode.
3. Iterate through the list and open each file in read mode.
4. Read the data from files and simultaneously write the data in file3.
5. Close all the files
Note: To successfully run the below program file1.txt and file2.txt must exist in the same folder.
"""

# Creating a list of filenames
filenames = ['file1.txt', 'file2.txt']

# Open file3 in write mode
with open('file3.txt', 'w') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from file1 and file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2 from next line
        outfile.write("\n")
