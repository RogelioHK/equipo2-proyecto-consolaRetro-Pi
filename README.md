# equipo2-proyecto-consolaRetro-Pi
 Repositorio con los archivos necesarios para crear una consola retro con la Raspberry Pi

Paquetes necesarios

sudo apt-get install git imagemagick python3-tk qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools qtbase5-dev-tools libxv-dev libsdl1.2-dev libao-dev libopenal-dev alsa-oss alsa-tools pulseaudio g++

Clonar el siguiente repositorio, el cual tiene el emulador de snes:

git clone https://github.com/devinacker/bsnes-plus.git

Entrar a la carpeta y aplicar make

cd ~/bsnes-plus/bsnes
make
