# PYTHON3 PROGRAM TO GRAB IMAGES FROM thispersondoesnotexist.com
# URL thispersondoesnotexist.com/image

# README
# loop is the number of image files you would want to download from the site
# sleep is for delay, by default 200 millisecond delay in the code, you can change the value to any time in seconds.

#INTRODUCTION TO THE PROGRAM

print("This is a program to download pictures from the website thispersondoesnotexist.com \n")
print("Written by Satish Luintel. github -> satishluintel \n")

# CODE STARTS HERE
# THIS CODE DOWNLOADS 4999 IMAGES.

import urllib3
import time	

http = urllib3.PoolManager()
loop = 1 

#START DOWNLOADING FILE 

while (loop<5000):
	
  r = http.request('GET', 'https://www.thispersondoesnotexist.com/image')
	if(r.status == 200):
		f = open(str(loop)+".jpg", "wb")
		f.write(r.data)
		f.close()
		print 'Success! File',loop,'has been downloaded !'
	print 'Sleeping 200 millisec ...\n'
	time.sleep(0.2)
	
  loop+=1
  
# END OF PROGRAM 
