import hashlib 

#*************************************************************************
#FUNCTION DEFINITIONS
#*************************************************************************
def hashfile(filename):
    """The function returns the SHA 256 hash of the file passed to it
    Args:
        filename ([type]): [description]
    """    
    #make a hash object
    h = hashlib.sha256()

    #open file for reading in binary mode
    with open (filename,'rb') as file: 

        #loop until end of file
        chunk = 0
        while chunk != b'':
            #read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
        #return the hex representation of the digest
        return h.hexdigest()
#*************************************************************************

#Ask user to put in the name of the file along with exe(title.txt)
print ("What is the file you want to check (put in title+extension) :")
fileInput = input()

#Ask user to put in the expected SHA256 hash for said file
print ("What is the expected sha-256 hash? (Copy expected and Right click): ")
hashInput = input()
hashInput = hashInput.lower()

message = hashfile(fileInput)

#Check to see if hashes match the expected
if hashInput == message: 
    print ("The hashes match! The file's integrity is True")
else: 
    print ("The hashes do NOT match. Please obtain the file again from the source!")


