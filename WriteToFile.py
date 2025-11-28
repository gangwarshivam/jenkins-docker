# 3.Write to a File
# Write a program to create a text file and write some content to it.
# Using file functions like write and open.


# creating sample.txt file
file=open("sample.txt","w")

# writing content in sample.txt
file.write("Hello! This is new file create using Python")

# closing the file
file.close()
