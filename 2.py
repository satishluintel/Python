

# PYTHON PROGRAM TO GRAB IMAGES FROM https://ph-avatars.imgix.net/
# URL thispersondoesnotexist.com/image
# README
# loop is the number of image files you would want to download from the site

#INTRODUCTION TO THE PROGRAM

print("This is a program to download pictures from the website thispersondoesnotexist.com \n")
print("Written by Satish Luintel. github -> satishluintel \n")


# CODE STARTS HERE

import urllib3
import time	

http = urllib3.PoolManager()

loop = 343434

while (loop<343438):

	URL = 'https://ph-avatars.imgix.net/'+str(loop)+'/original?auto=format&codec=mozpng&w=1632&h=1632'
	r = http.request('GET', URL)

	if(r.status == 200):
		f = open(str(loop)+".jpg", "wb")
		f.write(r.data)
		f.close()
		print('Success! File',loop,'has been downloaded !')

	loop+=1

# END OF PROGRAM 
