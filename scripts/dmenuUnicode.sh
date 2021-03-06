#!/bin/sh
# Give dmenu list of all unicode characters to copy.
# Shows the selected character in dunst if running.

emoticon=$(cat ~/dotfiles/scripts/data/unicode | rofi -dmenu -config ~/dotfiles/i3/rofi.rasi | awk '{print $1}' | tr -d '\n' | xclip -selection clipboard)

pgrep -x dunst >/dev/null && notify-send "$(xclip -o -selection clipboard) copied to clipboard."
