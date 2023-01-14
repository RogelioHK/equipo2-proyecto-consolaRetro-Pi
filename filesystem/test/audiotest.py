import os
import threading
import multiprocessing
import time

#def sound():
#	p0 = multiprocessing.Process(target = os.popen, args = ["play /home/equipo2/filesystem/audios/Positive.ogg"])
#	p0.start()
#
#	time.sleep(2.5)
#	p0.terminate()


#t0 = threading.Thread(target = sound, args=())
#t0.start()

#print(os.popen("whoami").readlines())

USER_DIR = "/home/" + os.popen("whoami").readlines()[0].split("\n")[0] + "/"
print(USER_DIR)
