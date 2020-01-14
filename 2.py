

# PYTHON PROGRAM TO GRAB IMAGES FROM https://ph-avatars.imgix.net/
# loop is the number of image files you would want to download from the site

#INTRODUCTION TO THE PROGRAM

print("This is a program to download profile pictures from the website producthunt.com  \n")
print("Written by Satish Luintel. github -> satishluintel \n")

# CODE STARTS HERE

import urllib3
import time	

http = urllib3.PoolManager()

loop = 343434  #starting from 343434, you can start it from 0 and end the loop at n, where n is your desired number

while (loop<343464):

	URL = 'https://ph-avatars.imgix.net/'+str(loop)+'/original?auto=format&codec=mozpng&w=1632&h=1632'
	r = http.request('GET', URL)

	if(r.status == 200):
		f = open(str(loop)+".jpg", "wb")
		f.write(r.data)
		f.close()
		print('Success! File',loop,'has been downloaded !')

	loop+=1

# END OF PROGRAM 
