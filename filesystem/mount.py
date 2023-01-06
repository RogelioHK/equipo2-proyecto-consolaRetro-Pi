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
		#print("\tNo Storage")
		return None

#Function to mount the external drive, copy the Rom files and umount the external drive
def getFiles(drive, actualRoms):
	newRoms = []
	#print("Storage mounted: " + drive + " " + EXTERNAL_STORAGE)
	os.system("sudo mount " + drive + " " + EXTERNAL_STORAGE)
	data = os.popen("ls " + EXTERNAL_STORAGE + "ROMS/").readlines()
	#print("Read: ", data)
	for rom in data:
		rom = rom.split("\n")[0]
		if ".SMC" in rom and rom not in actualRoms:
			newRoms.append(rom)
			os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/*.SMC ~/ROMS/")
		elif ".smc" in rom and rom not in actualRoms:
			newRoms.append(rom)
			os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/*.smc ~/ROMS/")
		elif ".sfc" in rom and rom not in actualRoms:
			newRoms.append(rom)
			os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/*.sfc ~/ROMS/")
		elif ".SFC" in rom and rom not in actualRoms:
			newRoms.append(rom)
			os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/*.SFC ~/ROMS/")
		elif ".png" in rom:
			os.system("sudo cp " + EXTERNAL_STORAGE + "ROMS/*.png ~/ROMS/")
	#print("Files copied. ", newRoms, " added to the local ROMS")
	time.sleep(1)
	os.system("sudo umount " + EXTERNAL_STORAGE)
	os.system("sudo eject " + drive)
	#print("umounted storage. Remove the storage")
	while(isAvailableDrive()):
		os.system("sudo eject " + drive)
		time.sleep(10)
	return newRoms
