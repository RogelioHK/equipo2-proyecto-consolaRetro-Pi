import os
import time

#print("Mounts", os.system("blkid"))
EXTERNAL_STORAGE = "~/external-storage/"


def isAvailableDrive():
	#Read the storages connected to the RB
	storages = os.popen("sudo blkid").readlines()
	#If the available storages more than 2, exist an external drive to read
	if(len(storages) > 2):
		drive = storages[2].split(":")[0]
		#return the external drive's directory (sdx)
		return drive
	else:
		print("No Storage")
		return None

#Function to mount the external drive, copy the Rom files and umount the external drive
def getFiles():
	#Indicate if a external drive exist
	drive = isAvailableDrive()
	if(drive):
		print("Storage mounted: " + drive + " " + EXTERNAL_STORAGE)
		os.system("sudo mount " + drive + " " + EXTERNAL_STORAGE)
		data = os.popen("ls " + EXTERNAL_STORAGE).readlines()
		print(data)
		os.system("sudo cp "+ EXTERNAL_STORAGE + "*.SMC ~/ROMS/")
		print("Files copied")
#		#os.system("")
		os.system("sudo umount " + EXTERNAL_STORAGE)
		print("umounted storage")
getFiles()
