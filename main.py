# *********************************
#  CREATED BY LAKSHIT SOMANI
# *********************************


import requests
import random
import shutil
import sys

file1 = open("wallpapers.txt","a+")
numbers = set()
for line in open('wallpapers.txt',"r"):             
    try:                                                                        
        i = int(line)
        numbers.add(i)
    except ValueError:       
        print("Cannot convert from string to int")  
        continue 


def getWP():
    imageNumber = random.randint(1,4049)
    filename = str(imageNumber) + ".jpg"
    if imageNumber not in numbers:
        file1.write(str(imageNumber) + "\n")
        s = "https://wallpaper.infinitynewtab.com/wallpaper/" + str(imageNumber) + ".jpg"
        response = requests.get(s,stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            with open(filename,'wb') as f:
                shutil.copyfileobj(response.raw, f)
                print("Image downloaded successfully: "+filename)
        
        else:
            print('Image Couldn\'t be retreived')
    
    else:
        flag=0
        count=0
        for j in range(1,4050):
            if j not in numbers:
                flag=1
                count=+1
        if flag==0:
            print("!! ALL IMAGES FROM DATABASE ALREADY DOWNLOADED !!")
            print("!! NO MORE IMAGES CAN BE DOWNLOADED !!")
            sys.exit()
        else:
            for _ in range(count):
                getWP()


numberOfWallpapers = int(input("Enter number of wallpapers to be downloaded: "))
if numberOfWallpapers <= 4000:
    for _ in range(numberOfWallpapers):
        getWP()

file1.close()

