#MIT License

#Copyright (c) [2022] [Andrade Lopez Lesly Beatriz, Hernández Ku Rogelio, Lara Mandujano Diego Abraham]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import time
EXTERNAL_STORAGE = "~/external-storage/" #Directory for the external storage

#Function to verify if a new storage connected to the Pi
def isAvailableDrive():
	#Read the storages connected to the RBPi
	storages = os.popen("sudo blkid").readlines()
	#If the available storages more than 2, exist an external drive to read
	if(len(storages) > 2):
		drive = storages[2].split(":")[0]
		#return the external drive's directory (sdx)
		return drive
	else:
		return None

#Function to mount the external drive, copy the Rom files and umount the external drive
def getFiles(drive, actualRoms):
	newRoms = []
	#Mount the external storage in the "external-storage directory"
	os.system("sudo mount " + drive + " " + EXTERNAL_STORAGE)
	storage = os.popen("ls " + EXTERNAL_STORAGE).readlines()
	#Search for a "ROMS" directory. If doesn't exist, the script ends. If exist, copy the ROMs files
	if "ROMS\n" in storage:
		data = os.popen("ls " + EXTERNAL_STORAGE + "ROMS/").readlines()
		#Copy all the file which the extension is .SMC, .smc, .sfc, .SFC and .png. The ROMS files and the snes cover
		for rom in data:
			rom = rom.split("\n")[0]
			if ".SMC" in rom and rom not in actualRoms:
				newRoms.append(rom)
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + rom + "\" ~/ROMS/")
			elif ".smc" in rom and rom not in actualRoms:
				newRoms.append(rom)
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + rom + "\" ~/ROMS/")
			elif ".sfc" in rom and rom not in actualRoms:
				newRoms.append(rom)
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + rom + "\" ~/ROMS/")
			elif ".SFC" in rom and rom not in actualRoms:
				newRoms.append(rom)
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + rom + "\" ~/ROMS/")
			if ((rom.split(".")[0] + ".png\n") in data) and (rom in newRoms): #Copy the cover if exist
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + rom.split(".")[0] + ".png\" ~/ROMS/")
		#Check if the covers of the roms in the system exist in the external storage and copy it
		for cover in actualRoms:
			cover = cover.split(".")[0] + ".png"
			if cover + "\n" in data:
				os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/\"" + cover + "\" ~/ROMS/")
	else:
		newRoms.append("NoROM")
	#Check if the external storage is mounted. If it's true, then umount and eject it.
	while(isAvailableDrive()):
		try:
			os.popen("sudo umount " + EXTERNAL_STORAGE)
			os.popen("sudo eject " + drive)
		except:
			time.sleep(0.1)
	return newRoms
