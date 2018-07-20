#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

[ -f ~/.profile ] && source ~/.profile

export VAGRANT_DEFAULT_PROVIDER=virtualbox

export ANSIBLE_NOCOWS=1

alias avd='ansible-vault decrypt --vault-password-file=~/.vaultpw'
alias ave='ansible-vault encrypt --vault-password-file=~/.vaultpw'
alias aved='ansible-vault edit --vault-password-file=~/.vaultpw'
alias avv='ansible-vault view --vault-password-file=~/.vaultpw'

ldap-lookup() {
  ldapsearch -H ldap://dc1-mp.corp.surveymonkey.com -x -b "OU=SurveyMonkey,DC=corp,DC=surveymonkey,DC=com" -D "CORP\marca" -W sAMAccountName=$1
}

# Customize to your needs...
# if docker-osx > /dev/null; then
#     eval `docker-osx env`
# fi

# if boot2docker version > /dev/null; then
#   $(boot2docker shellinit 2> /dev/null)
# fi

# eval $(docker-machine env)

# alias ssh=sshrc
alias os-tenant='env | egrep --color=never "OS_(AUTH_URL|TENANT|USERNAME)"'

# BSD ls colors
export LSCOLORS='ExGxCxDxCxegedabagacad'

# BSD ls options
alias ls='ls -FG'

# GNU ls colors
export LS_COLORS="di=34;01:ln=36;01:so=32:pi=33:ex=31:bd=36;01:cd=33;01:su=31;40;07:sg=36;40;07:tw=32;40;07:ow=33;40;07"

# Zsh completion colors
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':prezto:module:completion:*' case-sensitive
zstyle ':completion:*' matcher-list 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# PATH
# export PATH=~/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/3.3/bin:/Library/Frameworks/Python.framework/Versions/3.2/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/npm/bin
# export PATH=~/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:/Library/Frameworks/Python.framework/Versions/2.6/bin:/Library/Frameworks/Python.framework/Versions/2.5/bin:/Library/Frameworks/Python.framework/Versions/2.4/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/Library/Frameworks/Python.framework/Versions/3.3/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/npm/bin
# CDPATH
CDPATH=.:~/dev/adobe:~/dev/git-repos:~/dev/hg-repos:~/go/src/git.corp.adobe.com/adobe-platform

# GoLang
export GOPATH=~/go
export PATH=$GOPATH/bin:$PATH

###
### Toggle prompt
#
ZPREZTO_FANCY_PROMPT="steeef"
ZPREZTO_PLAIN_PROMPT="redhat"

autoload -Uz promptinit
promptinit
prompt ${ZPREZTO_FANCY_PROMPT}

function current_prompt {
  prompt -c | awk 'NR == 2 { print $1 }'
}
function prt {
  if [[ "$(current_prompt)" == "${ZPREZTO_FANCY_PROMPT}" ]]; then
    prompt ${ZPREZTO_PLAIN_PROMPT}
  elif [[ "$(current_prompt)" == "${ZPREZTO_PLAIN_PROMPT}" ]]; then
    prompt ${ZPREZTO_FANCY_PROMPT}
  fi
}
###

title() { echo -en "\033]0;${*}\007"; }

# set tab title to cwd
precmd () {
  tab_label=$(basename ${PWD/${HOME}/\~}) # use 'relative' path
  # tab_label="$PWD:h:t/$PWD:t"
  echo -ne "\e]2;${tab_label}\a" # set window title to full string
  echo -ne "\e]1;${tab_label: -24}\a" # set tab title to rightmost 24 characters
}

# Python pip
# DEPRECATION: --download-cache has been deprecated and will be removed in the
# future. Pip now automatically uses and configures its cache.
# export PIP_DOWNLOAD_CACHE=~/.pip/download-cache

# Python virtualenvwrapper
export WORKON_HOME=~/python/virtualenvs
if which virtualenvwrapper.sh > /dev/null; then
  source $(which virtualenvwrapper.sh)
fi

# If a virtualenv activated, reactivate to get its path mods back
if [ ! -z $VIRTUAL_ENV ]; then
  source $VIRTUAL_ENV/bin/activate
fi

if [ -f ${HOME}/devpi/bin/devpi-ctl ]; then
  alias devpi-ctl="${HOME}/devpi/bin/devpi-ctl"
fi

# export PYTHONSTARTUP=~/.pythonrc.py
# alias python='PYTHONSTARTUP=~/.pythonrc.py python'

alias dc='docker-compose'
alias dm='docker-machine'
alias docker-logs-truncate="docker-machine ssh default -- 'sudo find /var/lib/docker/containers/ -iname \"*json.log\"|xargs -I{} sudo dd if=/dev/null of={}'"
alias dlt=docker-logs-truncate
alias gpr='hub pull-request'
alias gb='git branch -v'
alias gb2m='git checkout master && git fetch --all && git rebase origin/master'
alias gcam='git commit --verbose --amend'
alias gcom='git checkout master'
alias gph='git push origin HEAD'
alias gpo='git push origin'
alias gpfo='git push --force origin'
alias gr='git rebase'
alias grom='git rebase origin/master'
alias grls='git remote -v'
alias gwho='git shortlog -n -s --no-merges'
alias gws='git status --short --branch --untracked-files=no'
alias h='fc -i -D -l -1000000 | LESS="" less +G'
alias ipy='ipython'
alias mkve='mkvirtualenv'
alias pi='pip install'
pipun() {
  pip uninstall --verbose --yes "$@"
  if pip freeze | grep "$@"; then
    pip uninstall --verbose --yes "$@"
  fi
}
alias psd='pserve development.ini'
alias psdl='pserve development_local.ini'
alias py='python'
pyclean() {
  find . \( -name '*.pyc' -or -name '__pycache__' \) -exec rm -rf {} +
}
pys() {
  python -c 'import setuptools; execfile("setup.py")' "$@"
}
alias rerc='source ~/.zshrc'
alias sba='source bin/activate'
alias vim='mvim -v'

# Make Ctrl-Left and Ctrl-Right go backward/forward by words
# Sorin won't accept PR for prezto
# See: https://github.com/sorin-ionescu/prezto/issues/278
bindkey "^[[1;5D" emacs-backward-word
bindkey "^[[1;5C" emacs-forward-word
bindkey "h" vi-backward-word
bindkey "l" vi-forward-word
bindkey "?" run-help

# Make up and down arrows only use local history
# (don't share history from other zsh sessions - e.g.: tabs)
# from http://superuser.com/questions/446594/separate-up-arrow-lookback-for-local-and-global-zsh-history
if [ ! -z "${key_info[Up]}" ]; then
  bindkey "${key_info[Up]}" up-line-or-local-history
fi
if [ ! -z "${key_info[Down]}" ]; then
  bindkey "${key_info[Down]}" down-line-or-local-history
fi

up-line-or-local-history() {
    zle set-local-history 1
    zle up-line-or-history
    zle set-local-history 0
}
zle -N up-line-or-local-history
down-line-or-local-history() {
    zle set-local-history 1
    zle down-line-or-history
    zle set-local-history 0
}
zle -N down-line-or-local-history

# Don't exit shell when hit Ctrl-D
setopt ignoreeof

# Clobber existing files when redirecting output to a file
setopt CLOBBER

PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting

# Set up direnv (http://direnv.net/)
if direnv > /dev/null; then
    eval "$(direnv hook zsh)"
fi

# _docker_ip_hook() {
#   export DOCKER_IP=$(echo ${DOCKER_HOST:-tcp://127.0.0.1:2376} | cut -d/ -f3 | cut -d: -f1)
#   if [ "$DOCKER_IP" != "$OLD_DOCKER_IP" ]; then
#     echo "DOCKER_IP: $DOCKER_IP"
#   fi
#   OLD_DOCKER_IP=$DOCKER_IP
# }
# typeset -ag precmd_functions;
# if [[ -z ${precmd_functions[(r)_docker_ip_hook]} ]]; then
#   precmd_functions+=_docker_ip_hook;
# fi
