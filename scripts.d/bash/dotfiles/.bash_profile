[ -r ~/.bashrc ] && . ~/.bashrc
[ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion

export PATH=~/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Wireshark.app/Contents/MacOS

test -e "${HOME}/.iterm2_shell_integration.bash" && source "${HOME}/.iterm2_shell_integration.bash"
