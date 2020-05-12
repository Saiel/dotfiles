```
        _____       _      __   ____  ____  __________________    ___________
       / ___/____ _(_)__  / /  / __ \/ __ \/_  __/ ____/  _/ /   / ____/ ___/
       \__ \/ __ `/ / _ \/ /  / / / / / / / / / / /_   / // /   / __/  \__ \
      ___/ / /_/ / /  __/ /  / /_/ / /_/ / / / / __/ _/ // /___/ /___ ___/ /
     /____/\__,_/_/\___/_/  /_____/\____/ /_/ /_/   /___/_____/_____//____/
```

Here you can find my configs for different programs such like vim, zsh or kitty terminal.

## Installing

If you want easily install configs on your machine, you can just type
```shell
$ git clone https://github.com/Saiel/dotfiles.git
$ cd dotfiles
$ pip3 install pyyaml
$ python3 install.py
```

It reads `targets.yml` and copies choosen files into needed directories.

Also feel free to use this script in your repository.

### Configuring installation

* `source_dir` (required) - directory, where dotfiles stored.
* `targets` (required)
  * `<filename>` - name of dotfile, which wanted to copy.
    * `dir` (required) - installation directory for file.
    * `filename` (optional) - destination file name. If not provided, uses original file name.

## Feedback

Opening issues is very welcome, I always glad to get advices.
