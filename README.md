# equipo2-proyecto-consolaRetro-Pi
 Repositorio con los archivos necesarios para crear una consola retro con la Raspberry Pi

Actualizar repositorio y actualizar el software instalado:

<pre><code>sudo apt-get update</code></pre>
<pre><code>sudo apt-get upgrade</code></pre>

Paquetes necesarios

<pre><code>sudo apt-get install pip xinit matchbox-window-manager joystick git python3-tk qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools qtbase5-dev-tools libxv-dev libsdl1.2-dev libao-dev libopenal-dev alsa-oss alsa-tools python3-pil.imagetk pulseaudio g++</code></pre>
<pre><code>pip install pygame</code></pre>
<pre><code>pip install pyPS4Controller</code></pre>

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
<pre><code>cp ~/bsnes-plus/snesmusic/libsnesmusic.so ~/bsnes-plus/bsnes/out/</code></pre>
<pre><code>cp ~/bsnes-plus/snesreader/libsnesreader.so ~/bsnes-plus/bsnes/out/</code></pre>
<pre><code>cp ~/bsnes-plus/supergameboy/libsupergameboy.so ~/bsnes-plus/bsnes/out/</code></pre>

Ahora, debe configurar el emulador. Para ello, debe iniciarlo:
<pre><code>xinit ~/bsnes-plus/bsnes/out/bsnes</code></pre>

Dentro del emulador, se debe dirigir a la pestaña "settings" y después "configuration". Elija la pestaña "input" y configure sus controles dependiendo del gamepad o joystick con el que cuente. Después, en "advanced" cambie el "video driver" por "OpenGL" y active la opción "Use native OS file dialogs".
Después de esto, cierre el emulador y regrese a la carpeta de usuario con:
<pre><code>cd ~/</code></pre>

Después, use la siguiente línea para clonar el repositorio:
<pre><code>git clone https://github.com/RogelioHK/equipo2-proyecto-consolaRetro-Pi.git</code></pre>

Una vez clonado el repositorio, primero entre a la carpeta y copie el directorio "external-storage" en la carpeta "~/"
<pre><code>cd equipo2-proyecto-consolaRetro-Pi</code></pre>

Posterior a esto,  copie los directorios "filesystem" y "ROMS" a la carpeta "~/".
<pre><code>cp -r filesystem ~/</code></pre>
<pre><code>cp -r ROMS ~/</code></pre>

Además de esto, en la carpeta del usuario, debe crear un directorio "external-storage", ya que será el directorio por defecto en el cual se montarán las USB.
<pre><code>mkdir ~/external-storage</code></pre>

Ahora, para que la interfaz se cargue de incio en la Raspberry Pi abra el archivo .bashrc
<pre><code>nano .bashrc</code></pre>

y añada las siguientes líneas al final de este:

<pre><code>if [ -z "${SSH_TTY}" ]; then
	xinit ~/filesystem/startemu.sh >/dev/null 2>&1
fi</code></pre>

Una vez teniendo los directorios en su lugar, es necesario volver a abrir el emulador y entrar a la configuración n el apartado "Paths". Aquí se añadirán las carpetas necesarias para el funcionamiento del sistema.

En el apartado de "Games", elija la carpeta "home/equipo2/ROMS".
En el apartado "save RAM", elija "home/equipo2/filesystem/RAM-states"
El apartado "Save states, BPS/UPS/IPS patches, Cheat codes y Exported data" es opcional elegir.
En el apartado "Extra chip firmware", elija "home/equipo2/ROMS/firmaware".
Finalmente, salga del emulador.
<pre><code></code></pre>
