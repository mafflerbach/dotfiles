#!/bin/bash

sessions=$(ls -1 $HOME/.local/share/qutebrowser/sessions | rofi -dmenu -theme ~/dotfiles/i3/rofi.rasi)
if [ "$sessions" != "" ]; then
    qutebrowser ":session-load ${sessions/\.yml/}"
fi


