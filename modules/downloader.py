from re import search
from requests import get
from requests.exceptions import MissingSchema
from urllib.request import urlretrieve
from sys import argv

header = '''\033[35m
                ███████╗██████╗       ██████╗ ██╗     
                ██╔════╝██╔══██╗      ██╔══██╗██║     
                █████╗  ██████╔╝█████╗██║  ██║██║     
                ██╔══╝  ██╔══██╗╚════╝██║  ██║██║     
                ██║     ██████╔╝      ██████╔╝███████╗
                ╚═╝     ╚═════╝       ╚═════╝ ╚══════╝
                        \033[31mCoded by f4ll | 0.3
'''

def fbdownloader():
    try:
        if len(argv) >= 3:
            print(header)
            if argv[1] == '-l' or argv[1] == '--link':
                url = argv[2]
                response = get(url)

                if len(argv) >= 4:
                    if argv[3] == '-hd':
                        try:
                            link = search ('hd_src:"(.+?)"', response.text)[1]
                        except Exception:
                            print("\n\033[31m[-] This video doesn't have this quality, downloading the best quality.\033[m")
                            link = search ('sd_src:"(.+?)"', response.text)[1]
                    elif argv[3] == '-sd':
                        try:
                            link = search ('sd_src:"(.+?)"', response.text)[1]
                        except Exception:
                            print("\n\033[31m[-] This video doesn't have this quality.\033[m")
                            link = search ('hd_src:"(.+?)"', response.text)[1]
                    else:
                        print('\n\033[31m[-] Invalid argument, downloading best quality (File name argument before Quality argument).\033[m')
                        
                        try:
                            link = search ('hd_src:"(.+?)"', response.text)[1]
                        except Exception:
                            link = search ('sd_src:"(.+?)"', response.text)[1]
                    if len(argv) >= 6: 
                        if argv[4] == '-n' or argv[4] == '--name':
                            print('\n\033[32m[+] Downloading video...\033[m\n')
                            urlretrieve(link, f"{argv[5]}.mp4")
                            print('\033[32m[+] Download successfull.\033[m')
                        else:
                            print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                            print('\033[32m[+] Downloading video...\033[m\n')
                            urlretrieve(link, f"Facebook Video.mp4")
                            print('\033[32m[+] Download successfull.\033[m')
                    else:
                        print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                        print('\033[32m[+] Downloading video...\033[m\n')
                        urlretrieve(link, f"Facebook Video.mp4")
                        print('\033[32m[+] Download successfull.\033[m')
                else:
                    print('\n\033[31m[-] The quality was not stipulated, downloading best quality.\033[m')
                    try:
                        link = search ('hd_src:"(.+?)"', response.text)[1]
                    except Exception:
                        link = search ('sd_src:"(.+?)"', response.text)[1]
                    print('\n\033[31m[-] The file name was not stipulated, downloading with default file name.\033[m\n')
                    print('\033[32m[+] Downloading video...\033[m\n')
                    urlretrieve(link, f"Facebook Video.mp4")
                    print('\033[32m[+] Download successfull.\033[m')
            else:
                print('\n\033[31m[-] Invalid argument, first argument must be link argument.\033[m')
        else:
            print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m')
    except MissingSchema:
        print("\n\033[31m[-] This link doesn't redirect to a Facebook video.\033[m")
    except KeyboardInterrupt:
        print('\033[34mCoded by f4ll_py.\033[m\n')
    except TypeError:
        print(f'\n\033[31m[-] An error has occurred: Video unavailable.\033[m')
    except Exception as e:
        print(f'\n\033[31m[-] An error has occurred: {e}\033[m')