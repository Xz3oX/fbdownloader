#!/usr/bin/env python
try:
    from modules.downloader import fbdownloader
    from sys import argv

except Exception as e:
    print(f'\033[31m[-] An error has occurred with a module: \033[m{e}\n')

else:
    if argv[1] == '-h' or argv[1] == '--help':
            print('\n[+] Basic Commands:\n')
            print('[+]   -h                 Help')
            print('[+]   --help             Help')
            print('[+]   -l \033[33m{link}\033[m          Video Link')
            print('[+]   --link \033[33m{link}\033[m      Video Link')
            print('[+]   -hd                HD Quality')
            print('[+]   -sd                SD Quality')
            print('[+]   -n \033[33m{name}\033[m          File Name (Without spaces)')
            print('[+]   --name \033[33m{name}\033[m      File Name (Without spaces)')
            print('[+]   Sequency           Link > Quality > Name')
    else:
        try:
            fbdownloader()
            
        except IndexError:
            print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters. ( Sequency: Link > Quality > Name )\033[m')
