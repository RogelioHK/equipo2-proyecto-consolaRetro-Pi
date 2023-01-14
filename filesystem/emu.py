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
import threading
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Label, Entry, PhotoImage
from pyPS4Controller.controller import Controller
import mount


#Global variables
USER_DIR = "/home/" + os.popen("whoami").readlines()[0].split("\n")[0] + "/" #dinamic user
ROMS_DIR =  USER_DIR + "ROMS/" #dinamic user added to the ROMS dir
roms = [] #List of the roms in the system
actual = 0 #Variable which contains the actual position in the roms list
timeStart = 0 #Take the time when the ps button is pressed
timeEnd = 0 #Take the time when the ps button is unpressed
psRelease = False #Boolean variable which change to True when the ps button is unpressed
actualGame = threading.Thread() #Thread of the actual game in emu
isPlaying = False #Bool which change when the emu is on or off
isControl = False #Bool which change when the controll is connect of disconnect
untilPressed = False #Bool which change when the isUntilPressedFunction is Called
active = True # block the ps button until the game start

#Tkinter (GUI) objects
window = tk.Tk()	#Comment when using SSH
window['background']='#262626'
#labels and Image control. The parameter change the color, font, backgrouds color and position of the text
lbl0 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl0.place(x=10, y=10, width=1250, height = 50)

lbl1 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl1.place(x=855, y=620, width=400, height = 50)

lbl2 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl2.place(x=10, y=90, width=400, height = 50)

lbl3 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl3.place(x=10, y=140, width=400, height = 50)

lbl4 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl4.place(x=10, y=190, width=400, height = 50)

lbl5 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl5.place(x=10, y=240, width=400, height = 50)

lbl6 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl6.place(x=10, y=290, width=400, height = 50)

lbl7 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl7.place(x=10, y=340, width=400, height = 50)

lbl8 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl8.place(x=10, y=390, width=400, height = 50)

lbl9 = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbl9.place(x=10, y=440, width=400, height = 50)

lbla = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lbla.place(x=10, y=490, width=400, height = 50)

lblb = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lblb.place(x=10, y=540, width=400, height = 50)

lblc = Entry(window, bg="#333333", font = "Console 16", fg = "white", justify=tk.CENTER)
lblc.place(x=10, y=590, width=400, height = 50)

img = Image.open(USER_DIR + "filesystem/img/pd.png")
img = img.resize((100,100), Image.ANTIALIAS)
img0 = ImageTk.PhotoImage(img)
lbl_img = Label(window, image = img0, bg = "#333333")

img1 = Image.open(USER_DIR + "filesystem/img/pinguinostart.png")
img1 = img1.resize((100,100), Image.BICUBIC)
img2 = ImageTk.PhotoImage(img1)
lbl_img1 = Label(window, image = img2, bg = "#262626")

def lock():
	global active
	ts = time.time()
	te = 0
	while (te-ts) <= 5:
		te = time.time()
	active = True

#Class necesary for the map of the ps4 joystick (this recognize all gamepads, but use the ps4 joystick mapped)
class Control(Controller):
	def __init__(self, **kwargs):
		Controller.__init__(self, **kwargs)

	#Functions which defines the buttons action
	def on_playstation_button_press(self):
		global timeStart, timeEnd, psRelease, untilPressed, active

		if(active):
			timeStart = 0
			timeEnd = 0
			psRelease = False
			#Start the thread to determines how time is pressed this button. If pass the 1.5s, then close the game or shutdown the system
			untilPressed = False
			pressed = threading.Thread(target = isUntilPressed, args = ())
			pressed.start()
		else:
			os.popen("aplay ~/filesystem/audios/lock.wav")

	def on_playstation_button_release(self):
		global roms, actual, actualGame, psRelease, img1, img2, lbl_img1, isPlaying, untilPressd, active
		if active:
			psRelease = True
			#Ask if the emu is active
			if isPlaying == False and untilPressed == False:
				#Get the roms directory and execute a Thread of the emulation
				defRom = "~/bsnes-plus/bsnes/out/bsnes ~/ROMS/" + "\"" + roms[actual] + "\""
				actualGame = threading.Thread(target=os.system, args=[defRom])
				actualGame.start()
				isPlaying = True
				#Put the image in front of the GUI while the game start
				img1 = Image.open(USER_DIR + "filesystem/img/pinguinostart.png")
				img1 = img1.resize((300,300), Image.BICUBIC)
				img2 = ImageTk.PhotoImage(img1)
				lbl_img1 = Label(window, image = img2, bg = "#262626")
				lbl_img1.place(x = 0, y = -200, width = 1280, height = 1024)
				active = False
				stayGame = threading.Thread(target=lock, args=())
				stayGame.start()
#When the game is running, is unable. Otherwise, interact with the games list.
	def on_up_arrow_press(self):
		global isPlaying
		if isPlaying:
			pass
		else:
			updateActualRom(1)
			os.popen("aplay ~/filesystem/audios/select.wav")

	def on_down_arrow_press(self):
		global isPlaying
		if isPlaying:
			pass
		else:
			updateActualRom(-1)
			os.popen("aplay ~/filesystem/audios/select.wav")

	#Add a button to restart the system if any game is playing
	def on_share_press(self):
		global isPlaying
		if isPlaying:
			pass
		else:
			os.system("sudo reboot now")

#Functions to call when the control is connect and disconnect
def connect():
	global isControl, isPlaying
	updateLabels()
	if isPlaying == True:
		closeSystem()
	isControl = True #Change the joystick state to True

def disconnect():
	global isControl
	inputs = []
	while "js0\n" not in inputs: #If the Joystick doesn't connect, then wait for it
		isControl = False #Change the joystick state to False
		inputs = os.popen("ls /dev/input").readlines() #Read the directory
		#Show in the GUI that the joystick isn't available
		lbl0.delete(0, 'end')
		lbl0.insert(0, "")
		time.sleep(0.2)
		lbl0.delete(0, 'end')
		lbl0.insert(0, "Please connect the Gamepad")
		time.sleep(0.5)
	startControl()

#Function to start the joystick driver
def startControl():
	global isControl, lbl0
	try:
		#Connect the js0 input. If use two gamepads, only the first handle the interface
		c0 = Control(interface = "/dev/input/js0", connecting_using_ds4drv=False)
		c0.listen(on_connect=connect, on_disconnect=disconnect, timeout = 60) #Wait for the joystick for 60 seconds
	except:
		lbl0.delete(0, 'end')
		lbl0.insert(0, "Control Fail")
		startControl()

#Function to stop the thread of the game or shutdown the system
def closeSystem():
	global window, isPlaying, lbl_img1, active
	if isPlaying == True: #Means the emu is running. Then, they stopped
		os.popen("aplay ~/filesystem/audios/open.wav")
		os.system("sudo pkill bsnes") #Kill the thread of the emu "bsnes"
		isPlaying = False
		lbl_img1.place_forget()
	else:
		os.popen("aplay " + USER_DIR + "filesystem/audios/shutdown.wav")
		active = False
		time.sleep(2)
		os.system("sudo shutdown -h now")

#Function wich detect if the ps button is pressed until 1.5 second. The, use the closeSystem function
def isUntilPressed():
	global timeStart, timeEnd, psRelease, untilPressed
	timeStart = time.time()
	while psRelease == False:
		timeEnd = time.time()
		if((timeEnd - timeStart) >= 1.5):
			closeSystem()
			untilPressed = True
			return

#Function which update the next arg on the global roms list.
# If the arg on the list is > lenght list, return to 0.
# If the arg on the list is < 0, then return to the last arg of the list
def updateActualRom(num):
	global actual, roms
	actual += num
	if (actual >= len(roms)):
		actual = 0
	elif (actual < 0):
		actual = len(roms) - 1
	updateLabels()

#Function to change the Image for the image of the actual game (or use the default image if isn't)
#and update the list of games at the left side of the GUI when is necessary
def updateLabels():
	global roms, actual, img, img0, lbl0, lbl_img, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbla, lblb,lblc

	lbl0.delete(0, 'end')
	lbl0.insert(0, roms[actual].split(".")[0])
	lbl2.delete(0, 'end')
	lbl2.insert(0, roms[-len(roms) + actual + 1].split(".")[0])
	lbl3.delete(0, 'end')
	lbl3.insert(0, roms[-len(roms) + actual + 2].split(".")[0])
	lbl4.delete(0, 'end')
	lbl4.insert(0, roms[-len(roms) + actual + 3].split(".")[0])
	lbl5.delete(0, 'end')
	lbl5.insert(0, roms[-len(roms) + actual + 4].split(".")[0])
	lbl6.delete(0, 'end')
	lbl6.insert(0, roms[-len(roms) + actual + 5].split(".")[0])
	lbl7.delete(0, 'end')
	lbl7.insert(0, roms[-len(roms) + actual + 6].split(".")[0])
	lbl8.delete(0, 'end')
	lbl8.insert(0, roms[-len(roms) + actual + 7].split(".")[0])
	lbl9.delete(0, 'end')
	lbl9.insert(0, roms[-len(roms) + actual + 8].split(".")[0])
	lbla.delete(0, 'end')
	lbla.insert(0, roms[-len(roms) + actual + 9].split(".")[0])
	lblb.delete(0, 'end')
	lblb.insert(0, roms[-len(roms) + actual + 10].split(".")[0])
	lblc.delete(0, 'end')
	lblc.insert(0, roms[-len(roms) + actual + 11].split(".")[0])

	imgs = os.popen("ls " + ROMS_DIR).readlines()

	if (roms[actual].split(".")[0] + ".png\n") in imgs:
		img = Image.open(ROMS_DIR + roms[actual].split(".")[0] + ".png")
		img = img.resize((795,495), Image.ANTIALIAS)
		img0 = ImageTk.PhotoImage(img)
		lbl_img = Label(window, image = img0, bg = "#333333")
		lbl_img.place(x = 455, y = 90, width = 800, height = 500)
	else:
		print("IMGS: ", imgs)
		img = Image.open(USER_DIR + "filesystem/img/pd.png")
		img = img.resize((100,100), Image.BICUBIC)
		img0 = ImageTk.PhotoImage(img)
		lbl_img = Label(window, image = img0, bg = "#333333")
		lbl_img.place(x = 455, y = 90, width = 800, height = 500)

#Funtion to read the local ROMS directory and initialize de roms global list
def readActualRoms():
	global roms
	actualroms = os.popen("ls ~/ROMS/").readlines()
	for ar in actualroms:
		if ".SMC" in ar or ".smc" in ar or ".SFC" in ar or ".sfc" in ar:
			roms.append(ar.split("\n")[0])
	roms.sort()
	updateLabels()

#Function to read the external ROMS directory. For more information, read mount.py
def readRoms():
	global roms, lbl1
	data = 0
	while True:
		data =  mount.isAvailableDrive()
		if data:
			os.popen("aplay ~/filesystem/audios/plugged.wav")
			lbl1.delete(0, 'end')
			lbl1.insert(0, "Storage Detected. Reading...")
			updateRoms(mount.getFiles(data, roms))
			lbl1.delete(0, 'end')
			lbl1.insert(0, "Disconnect the Drive")
			os.popen("aplay ~/filesystem/audios/unplugged.wav")
		else:
			lbl1.delete(0, 'end')
			lbl1.insert(0, "No Storage Detected")
		time.sleep(1)

#Function to update the roms global list
def updateRoms(newRoms):
	global roms, lbl1
	if (len(newRoms) > 0): #Detect if the list of new roms is empty. Else, update the roms global list
		if ("NoROM" in newRoms): #Detect if the ROMS directory exist in the external-storage
			lbl1.delete(0, 'end')
			lbl1.insert(0, "No ROMS directory")
		else:
			lbl1.delete(0, 'end')
			lbl1.insert(0, "New ROMS Detected! Copying...")

			#Add the new roms name to the roms global list
			for nr in newRoms:
				if nr not in roms:
					roms.append(nr)
	else:
		lbl1.delete(0, 'end')
		lbl1.insert(0, "No new ROMS")
	roms.sort() #Sort the roms
	time.sleep(1) #Time to see the messages in the GUI

#Function to start the GUI
def startGui():
	global window
	window.geometry("1280x1024")
	window.mainloop()

#Main function which starts the threads of services necesaries
#for the correct functionality of the program
def main():
	os.popen("aplay ~/filesystem/audios/boot.wav")
	#sound("start") #Play the start sound
	readActualRoms() #Read the actual roms in the ROMS directory and append into the roms global list
	strControl = threading.Thread(target=startControl, args=())
	strControl.start() #Start the gamepad driver for the GUI
	externalDevice = threading.Thread(target = readRoms, args=())
	externalDevice.start() #Start the thread which read the external storage
	startGui() #Start the GUI

if __name__ == '__main__':
	main()
