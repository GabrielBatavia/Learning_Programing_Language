# try to open the file
file = open("my_file.txt")
content = file.read()

print(content)




# close the file to minimize memory usage
file.close()