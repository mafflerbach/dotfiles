nord = {
    # Polar Night
    'nord0': '#2e3440',
    'nord1': '#3b4252',
    'nord2': '#434c5e',
    'nord3': '#4c566a',
    # Snow Storm
    'nord4': '#d8dee9',
    'nord5': '#e5e9f0',
    'nord6': '#eceff4',
    # Frost
    'nord7': '#8fbcbb',
    'nord8': '#88c0d0',
    'nord9': '#81a1c1',
    'nord10': '#5e81ac',
    # Aurora
    'nord11': '#bf616a',
    'nord12': '#d08770',
    'nord13': '#ebcb8b',
    'nord14': '#a3be8c',
    'nord15': '#b48ead',
    }



# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')
# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

config.bind('<Ctrl-Shift-y>', 'hint links spawn --detach mpv --force-window yes {hint-url}')

config.bind('<Ctrl-Shift-p>', 'hint links spawn --verbose --detach /home/maren/dotfiles/i3/script/fillplaylist.sh push {hint-url}')

config.bind('<Ctrl-Shift-l>', 'hint links spawn --verbose --detach  youtube-dl {hint-url} --output /home/maren/Downloads/ytFiles/%(title)s.%(ext)s')

config.bind('<Ctrl-Shift-f>', 'hint links spawn --verbose --detach  /home/maren/Downloads/nzbmonkey-v0.2.5-linux/nzbmonkey.py {hint-url} ')

config.bind('<Ctrl-Shift-o>', 'spawn --verbose --detach /home/maren/dotfiles/i3/script/fillplaylist.sh play')

config.bind('<Ctrl-Shift-d>', 'hint links spawn --verbose --detach mpv {hint-url}')

config.set('content.headers.user_agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3029.110 Safari/537.36')

config.bind('<Ctrl-Shift-k>', 'open -t /home/maren/dotfiles/i3/script/translate.sh')

config.bind(',p', 'spawn --userscript qute-keepass -p ~/Documents/Database.kdbx')

config.source('/home/maren/dotfiles/qutebrowser/qutewal.py')
