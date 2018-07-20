# AWS & klam-ext
export AWS_DEFAULT_REGION="us-east-1"
[ -x ~/bin/klam-ext ] && ~/bin/klam-ext --version > /dev/null 2>&1 && eval "$(~/bin/klam-ext bash-integration)"

[ -f ~/.profile ] && source ~/.profile

# direnv
if which direnv > /dev/null; then eval "$(direnv hook bash)"; fi

export PS1='\h:\w> '

_docker_ip_hook() {
  export DOCKER_IP=$(echo ${DOCKER_HOST:-tcp://127.0.0.1:2376} | cut -d/ -f3 | cut -d: -f1)
  if [ "$DOCKER_IP" != "$OLD_DOCKER_IP" -a "$DOCKER_IP" != "127.0.0.1" ]; then
    echo "DOCKER_IP: $DOCKER_IP"
  fi
  OLD_DOCKER_IP=$DOCKER_IP
}

if ! [[ "$PROMPT_COMMAND" =~ _docker_ip_hook ]]; then
  PROMPT_COMMAND="_docker_ip_hook;$PROMPT_COMMAND";
fi
