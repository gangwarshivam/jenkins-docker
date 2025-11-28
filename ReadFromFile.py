# Read from a File
# We used open in read mode and file.read to read and print to display.

# opening file sample.txt created in previous code
file=open("sample.txt","r")

# reading content of file and storing in data variable
data=file.read()

# printing data to display file content
print(data)
