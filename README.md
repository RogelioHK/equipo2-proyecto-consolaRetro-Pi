# equipo2-proyecto-consolaRetro-Pi
 Repositorio con los archivos necesarios para crear una consola retro con la Raspberry Pi

Paquetes necesarios

<pre><code>sudo apt-get install xinit matchbox-window-manager joystick git python3-tk qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools qtbase5-dev-tools libxv-dev libsdl1.2-dev libao-dev libopenal-dev alsa-oss alsa-tools pulseaudio g++</code></pre>

Clonar el siguiente repositorio, el cual tiene el emulador de snes:

<pre><code>git clone https://github.com/devinacker/bsnes-plus.git</code></pre>

Entrar a la carpeta y aplicar make

<pre><code>cd ~/bsnes-plus/bsnes</code></pre>

Luego compile con el siguiente comando:
<pre><code>make</code></pre>

Una vez compilado el emulador, puede ejecutarse con el siguiente comando para probarlo:
<pre><code>xinit ~/bsnes-plus/bsnes/out/bsnes</code></pre>

Después, debe copiar los archivos snesfilter, snesmusic, snesreader y supergameboy de sus respectivas carpetas; las cuales se encuentran en el directorio <code>~/bsnes-plus</code>. Para copiarlos, siga las siguentes líneas:
<pre><code>cp ~/bsnes-plus/snesfilter/libsnesfilter.so ~/bsnes-plus/bsnes/out/</code></pre>
<pre><code></code></pre>
<pre><code></code></pre>

<pre><code></code></pre>
