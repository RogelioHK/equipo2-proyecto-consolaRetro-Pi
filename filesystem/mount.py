import os
import time

EXTERNAL_STORAGE = "~/external-storage/"

#Function to verify if a new storage connected to the Pi
def isAvailableDrive():
	#Read the storages connected to the RB
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
	os.system("sudo mount " + drive + " " + EXTERNAL_STORAGE)
	storage = os.popen("ls " + EXTERNAL_STORAGE).readlines()
	#Search for a "ROMS" directory. If doesn't exist, the script ends. If exist, copy the ROMs files
	if "ROMS\n" in storage:
		data = os.popen("ls " + EXTERNAL_STORAGE + "ROMS/").readlines()
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
		while(isAvailableDrive()):
			os.system("sudo umount " + EXTERNAL_STORAGE)
			os.system("sudo eject " + drive)
			time.sleep(3)
	else:
		newRoms.append("NoROM")
	return newRoms

#if isAvailableDrive():
#	getFiles("/dev/sda1", [])
