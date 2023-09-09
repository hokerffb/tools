export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
export PATH=$PATH:/usr/local/node16/bin:/usr/local/go/bin/

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias netstat='netstat'
alias cp='cp -i'
alias lis='netstat -an|grep tcp|grep --color LISTEN'
alias s='sudo netstat -antlp|grep tcp|grep LISTEN'
alias pm="iptables -t nat -L PREROUTING"

alias dockerps='docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"'
alias dps='docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"'
alias di='docker images'
alias dip="docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'"

export GO111MODULE=on
export GOPROXY=https://goproxy.io
export PATH=$PATH:/usr/local/go/bin

export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_COLLATE=C
export LC_CTYPE=en_US.UTF-8
