#!/bin/bash

echo "Cloning Raspimon_Academy project to ~/Desktop if it does not exist."
RASPIMON_DIR="$HOME/Desktop/Raspimon_Academy"

if [[ -e $RASPIMON_DIR ]];then
    echo "$RASPIMON_DIR already exists"
else
    cd ${RASPIMON_DIR%/Raspimon_Academy}
    git clone https://github.com/CodeNextAdmin/Raspimon_Academy.git
fi

ls -l $RASPIMON_DIR
xdg-open $RASPIMON_DIR

echo "Open the curriculum & project pages"
xdg-open https://codenext.withgoogle.com/curriculum?role=student&step=1 &
xdg-open https://github.com/CodeNextAdmin/Raspimon_Academy &

echo "Open Python Cheat Sheets"
xdg-open https://ehmatthes.github.io/pcc/cheatsheets/README.html &

echo "Open github CS"
xdg-open https://training.github.com/downloads/github-git-cheat-sheet &

echo "Open bash CS"
xdg-open https://devhints.io/bash &

echo "Open Linux commands CS"
xdg-open https://www.guru99.com/linux-commands-cheat-sheet.html &