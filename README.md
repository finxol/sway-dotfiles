# Sway Rice Dotfiles
Dotfiles are any files or directories starting with a "." in their name. They are commonly configuration files for software on your computer, such as the ".vimrc" for Vim and ".config", a common directory for software to have their configurations stored.

This is only a customisation from the dotfiles created by [zahimeen](https://github.com/zahimeen/dotfiles/tree/sway).

![Desktop](desktop.png)

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
