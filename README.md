# Sway Rice Dotfiles
Dotfiles are any files or directories starting with a "." in their name. They are commonly configuration files for software on your computer, such as the ".vimrc" for Vim and ".config", a common directory for software to have their configurations stored.

This is only a customisation from the dotfiles created by [zahimeen](https://github.com/zahimeen/dotfiles/tree/sway).

This whole repo is set under public domain thanks to the Unlicense.
Please feel free to copy and/or modify these files to your liking.

![Desktop](desktop.png)
![Desktop](desktop2.png)

## Setup
Install all the necessary packages
```bash
sudo dnf install sway rofi waybar alacritty light
```

Clone the repo and copy the contents of the .config directory to your home directory
```bash
git clone https://github.com/finxol/sway-rice.git
cp -r sway-rice/.config/* ~/.config/
```

You can also copy the contents of .zshrc and .profiles but it will still work perfectly without 

You can now reboot into sway and it should look nice
