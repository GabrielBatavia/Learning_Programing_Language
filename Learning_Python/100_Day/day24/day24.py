# try to open the file
#file = open("my_file.txt")
#content = file.read()

#print(content)

# close the file to minimize memory usage
#file.close()


## Another way with better performance
# with this way, we dont have to worry about close syntax
with open("my_file.txt") as file: 
    content = file.read()
    print(content)
    
