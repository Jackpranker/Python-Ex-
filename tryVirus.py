import os
os.getcwd()
change_dir= os.chdir("c:/Users/JackPranker/Pictures")
print(change_dir)
for i in range(100):
    #create_folder= os.mkdir("c:/Users/JackPranker/Pictures" + "/Jack!" + str(i))
    print("Virus Created")
print(os.getcwd())
change_dir= os.chdir("c:/Users/JackPranker/Pictures/Jack!1")
create_file= os.replace("File.txt.lnk","Pranker-virus.exe")
