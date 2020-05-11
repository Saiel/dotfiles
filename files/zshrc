#               __       _____       _      __
#   ____  _____/ /_     / ___/____ _(_)__  / /
#  /_  / / ___/ __ \    \__ \/ __ `/ / _ \/ /
#   / /_(__  ) / / /   ___/ / /_/ / /  __/ /
#  /___/____/_/ /_/   /____/\__,_/_/\___/_/
#

export PATH=$HOME/.local/bin:$PATH

# Path to oh-my-zsh installation.
export ZSH="/home/saiel/.oh-my-zsh"

ZSH_THEME="nt9"

CASE_SENSITIVE="false"

HYPHEN_INSENSITIVE="false"

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

DISABLE_AUTO_TITLE="false"

# Display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# HIST_STAMPS="mm/dd/yyyy"

plugins=(git
         ubuntu
         django
         pip
         sudo
         zsh-autosuggestions
         )

source $ZSH/oh-my-zsh.sh

# User configuration

alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias kittyconfig="vim ~/.config/kitty/kitty.conf"
alias vimconfig="vim ~/.vimrc"
alias sshconfig="vim ~/.ssh/config"
alias configheader="figlet -f slant"

# Autosuggest settings
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=245,bg=#222222'
export ZSH_AUTOSUGGEST_HISTORY_IGNORE='?(#c10,)'
export ZSH_AUTOSUGGEST_USE_ASYNC='True'
source /home/saiel/.zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
prompt_context() {}

autoload -Uz compinit
compinit
# Completion for kitty {{
if [[ $TERM == "xterm-kitty" ]]; then
    kitty +complete setup zsh | source /dev/stdin
    # alias cptermi='cptermi(){ infocmp xterm-kitty | ssh $1 tic -x -o \~/.terminfo /dev/stdin; }; cptermi'
    alias kssh="kitty +kitten ssh"
fi
# }}
