
# HomeBrew
export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
export PATH="/usr/local/bin:$PATH"
export PATH="/usr/local/sbin:$PATH"
# HomeBrew END

autoload -Uz compinit && compinit
alias ll='ls -l'

# git info
function git_branch {
   branch="`git branch 2>/dev/null | grep "^\*" | sed -e "s/^\*\ //"`"
   if [ "${branch}" != "" ];then
       if [ "${branch}" = "(no branch)" ];then
           branch="(`git rev-parse --short HEAD`...)"
       fi
       echo "($branch)"
   fi
}

autoload -U colors && colors
PS1="%n@%m %1~%{$fg[yellow]%}$(git_branch)%{$reset_color%} %# "
