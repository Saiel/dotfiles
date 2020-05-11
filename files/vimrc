" #################################################
" #   _    ___              _____       _      __ #
" #  | |  / (_)___ ___     / ___/____ _(_)__  / / #
" #  | | / / / __ `__ \    \__ \/ __ `/ / _ \/ /  #
" #  | |/ / / / / / / /   ___/ / /_/ / /  __/ /   #
" #  |___/_/_/ /_/ /_/   /____/\__,_/_/\___/_/    #
" #################################################

set nocompatible
filetype off

set rtp+=~/.vim/bundle/vundle/

call vundle#rc()

filetype plugin indent on

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'preservim/nerdtree'
Plugin 'majutsushi/tagbar'
Plugin 'leafgarland/typescript-vim'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'

let g:airline_solarized_bg = 'dark'
let g:airline_solarized_dark_inactive_background = 1
let g:airline_powerline_fonts = 1

set number
"colorscheme default

set shiftwidth=4
set softtabstop=4
set smarttab
set expandtab
set wildmenu
set updatetime=0

set ignorecase
set smartcase

set ruler

set visualbell
set t_vb=

set laststatus=2

if version >= 700
    set history=64
    set undolevels=128
    set undodir=~/.vim/undodir/
    set undofile
    set undolevels=1000
    set undoreload=10000
endif

augroup vimrc-incsearch-highlight
    autocmd!
    autocmd CmdlineEnter /,\? :set hlsearch
    autocmd CmdlineLeave /,\? :set nohlsearch
augroup END

autocmd vimenter * AirlineTheme raven
nmap <C-n> :NERDTreeToggle<CR>
nmap <F8> :TagbarToggle<CR>

set conceallevel=2

highlight Folded ctermfg=0
highlight Folded ctermbg=6

