# Appendiing to a existing python.py file

file1 = open('python.py', 'a')
print("Enter the data to be appended: ")
file1.write(input())
file1.write("\n")
file1.close()


# Reading the entire data from python.py

file1 = open("python.py", "r")
print("Output of Readlines after appending: ")
content = file1.read()
print(content)
file1.close()
