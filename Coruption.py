import os
# os.chdir("C:/Users/JackPranker/Pictures")
# destination= '"C:/Users/JackPranker/Documents/New Folder/"'
root= '"C:/Users/JackPranker/Downloads/new Fontss/"'
# print("+++++++++++++++Back up started++++++++++++++++++++")
# os.system('Copy ' + destination +' ' + root+ '')
# print("+++++++++++++++Back up Finished++++++++++++++++++++")
os.chdir("C:/Users/JackPranker/Downloads/new Fontss/")
print(os.getcwd())
if 'Will-Harris.ttf' in os.listdir():
    os.rename('Will-Harris.ttf.exe','Will-Harris.ttf')