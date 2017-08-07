#!/bin/bash

echo 'ElementaryOS 0.4.1 Loki快速上手配置脚本'
echo '本脚本将会帮你：'
echo '更新系统 && 安装软件源设置程序'

read -p '是否继续？(Y/N，默认=Y)：' confirm
case $confirm in
  N | n)
  exit 0;;
  *)

  echo '更新系统 && 安装软件源设置程序'
  sudo apt -y update && sudo apt -y upgrade
  sudo apt install software-properties-common software-properties-gtk -y


  echo '笔记本调整屏幕默认亮度操作'
    sudo apt -y install xbacklight
    xbacklight = 40%

  echo '安装 fcitx 框架操作'
    sudo apt install -y fcitx fcitx-table-wubi-large fcitx-frontend-all fcitx-frontend-gtk2 fcitx-frontend-gtk3 fcitx-frontend-qt4 fcitx-config-gtk fcitx-ui-classic fcitx-module-kimpanel fcitx-module-dbus libopencc1 fcitx-libs-qt fcitx-libs im-config wget
    clear
    echo "请在设置向导中选择fcitx为默认输入法框架，第二步请选择“Yes”"
    echo ""
    im-config

  echo '安装 fcitx-rime'
    sudo apt install -y fcitx-rime
    cp /usr/share/rime-data/wubi86.schema.yaml ~/.config/fcitx/rime/
    ln -s /usr/share/rime-data/wubi86.dict.yaml ~/.config/fcitx/rime/
    ln -s /usr/share/rime-data/wubi86.* ~/.config/fcitx/rime/

    vim ~/.config/fcitx/rime/detault.yaml
    # schema_list下加一行:
    - schema:wubi86

    echo "正在安装文泉驿字体套件"
    sudo apt install -y fonts-wqy-microhei ttf-wqy-microhei

  echo ' steam 字体包(解决字体方块)'
    sudo apt install -y fonts-wqy-zenhei

  echo "正在安装 Elementary Tweaks"
    sudo add-apt-repository -y ppa:philip.scott/elementary-tweaks
    sudo apt update
    sudo apt -y install elementary-tweaks

  echo "正在安装 Elementary Full 图标主题"
    sudo apt -y install git
    git clone https://github.com/btd1337/elementary-full-icon-theme
    sudo mv elementary-full-icon-theme /usr/share/icons/
    gsettings set org.gnome.desktop.interface icon-theme "elementary-full-icon-theme"
    sudo rm -rf elementary-full-icon-theme
    clear
  echo "正在安装 Arc 主题"
    sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/Horst3180/xUbuntu_16.04/ /' > /etc/apt/sources.list.d/arc-theme.list"
    sudo apt-key adv --recv-keys --keyserver keyserver.Ubuntu.com BEB6D886
    sudo apt update
    sudo apt -y install arc-theme
    clear
  echo "正在安装 Paper 主题"
    sudo add-apt-repository -y ppa:snwh/pulp
    sudo apt update
    sudo apt install -y paper-gtk-theme paper-icon-theme


  echo "正在安装压缩文件支持库"
    sudo apt -y install zip unzip p7zip p7zip-rar rar unrar

  echo "正在安装受版权保护软件包"
    sudo apt -y install ubuntu-restricted-extras
    clear

  echo "正在安装火狐浏览器"
    sudo apt -y install firefox
    clear
    echo "正在卸载系统自带浏览器"
    echo ""
    sudo apt remove --purge epiphany-browser epiphany-browser-data -y

  echo 'oh-my-zsh'
    sudo apt -y install git
    wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

  echo "正在安装BleachBit系统清理工具"
    echo ""
    sudo apt -y install bleachbit

  echo "正在安装LibreOffice"
    echo ""
    sudo apt -y install libreoffice

  echo "正在Shutter"
    echo ""
    sudo apt -y install shutter
  echo "Remove screenshot-tool"
    sudo apt remove -y screenshot-tool

  echo "正在安装aria2"
    echo ""
    sudo apt -y install aria2

  echo "正在安装Shotwell"
    echo ""
    sudo apt install -y shotwell

  echo "正在安装GParted"
    echo ""
    sudo apt -y install gparted

  echo "正在修复损坏的软件包"
    echo ""
    sudo apt -y -f install

  echo 'pyenv'
    curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

  echo 'tilda 下拉 terminal'
    sudo apt -y install tilda

  echo 'arc-theme'
    sudo add-apt-repository ppa:noobslab/themes
    sudo apt-get update
    sudo apt-get -y install arc-theme

  echo 'numix-icon-theme-circle'
    sudo apt-add-repository ppa:numix/ppa
    sudo apt-get update
    sudo apt-get -y install numix-icon-theme-circle

  echo 'variety 壁纸自动切换软件'
    sudo apt -y install variety

  echo 'powerline-font install'
    git clone https://github.com/powerline/fonts.git
  echo 'install '
    cd  fonts
    ./install.sh

  echo 'htop install'
    sudo apt -y install htop

  echo 'nvidia install'
    sudo vim /etc/modprobe.d/blacklist.conf
    echo '最后一行增加'
    echo 'blacklist nouveau'

    sudo apt search nvidia
    echo '安装最新版'
      sudo apt install -y nvidia-376 nvidia-prime

  echo 'pip install'
    sudo apt -y install python-pip

  echo 'eOS 与 window 相差8小时'
    sudo apt install -y ntpdate
    sudo ntpdate time.windows.com

    时间更新到硬件上:
    sudo hwclock --localtime --systohc

  echo '安装steam'
    sudo add-apt-repository multiverse
    sudo apt update
    sudo apt -y install steam

  echo '隐藏Applications图标'
    cd /usr/share/Applications
    ls
    将不想显示的图标
    cp xxx.desktop ~/.local/share/applications
    vim ~/.local/share/applications/xxx.desktop
    在最后加上一行：
    NoDisplay=true

    在自己的系统配置到差不多的时候，可以
      $ sudo apt-mark showmanual > .install
      在需要重装系统的时候，执行
      $ sudo apt-get install $(cat .install)
      就可以安装之前选择的所有软件了～

  echo "正在清理软件包"
    echo ""
    sudo apt -y autoremove
    sudo apt -y autoclean

  clear
  echo "配置完成，部分配置重启后生效。"

  read -p '配置完成，是否立即重启使部分配置生效？(Y/N，默认=N)：' reboot_confirm
  case $reboot_confirm in
    Y | y )
    sudo reboot;;
    * )
    exit 0;;
  esac
esac
