#Put this lines into the .bashrc
if [ -z "${SSH_TTY}" ]; then
	xinit ~/filesystem/startemu.sh -- -nocursor >/dev/null 2>&1
fi