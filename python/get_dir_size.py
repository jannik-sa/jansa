from glob import glob
import os



#simport sys
#start_dir = sys.argv[1]

übergabe = input("Wo willst du wissen wie viele dateien dort gesteichert werden ? \n")
start_dir = übergabe 

data = 0
ordner = 0
byte = 0

for root, dirs, files in os.walk(start_dir):    
    #print("root=%s" % root)
    #print("dirs=%s" % dirs)
    #print("files=%s" % files)
    "files=%s" % files
    "dirs=%s" % dirs
    "root=%s" % root
    for wenlist in range(len(files)):
        files2 = files[wenlist]
        weiterleiter = os.path.join(root,files2)
        props = os.stat(weiterleiter)
        byte += props[6]
        wenlist += 1
    data += len(files)
    ordner += len(dirs)
print("Datein:", data)
print("Unterordner:", ordner)
print("Bytes:",byte)
gigabyt = byte / (1024 * 1024 * 1024)
print("GB:", gigabyt)
  
 
   