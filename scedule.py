import os
import time

currenttime= time.strftime("%Y%m%d%H%I%S")
os.chdir("C:/Users/JackPranker/Desktop/")
current_wd=os.getcwd()
#os.mkdir("/Database")
#os.mkdir("/Application")
#os.mkdir(current_wd+"/Back_up")
#os.mkdir(current_wd+"/Back_up" +'/'+currenttime)
Database='Database'
Back_up='Back_up'

os.system('copy ' + Database+ '' + Back_up+'')