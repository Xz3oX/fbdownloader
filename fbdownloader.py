try:
    from re import search
    from requests import get
    from requests.exceptions import MissingSchema
    from urllib.request import urlretrieve
    from sys import argv

except KeyboardInterrupt:
    print('\n\033[34mCoded by f4ll_py.\033[m\n')
except Exception as e:
    print(f'\033[31m[-] An error has occurred with a module: \033[m{e}\n')
else:
    def fbdownloader(arg1, arg2, arg3, arg4, arg5):
        if len(argv) == 2:
            if arg1 == '-h' or arg1 == '--help':
                print('\n[+] Basic Commands:\n')
                print('[+]   -h                 Help')
                print('[+]   --help             Help')
                print('[+]   -l \033[33m{link}\033[m          Video Link')
                print('[+]   --link \033[33m{link}\033[m      Video Link')
                print('[+]   -hd                HD Quality')
                print('[+]   -sd                SD Quality')
                print('[+]   -n \033[33m{name}\033[m          File Name (Without spaces)')
                print('[+]   --name \033[33m{name}\033[m      File Name (Without spaces)')
            else:
                print('\n[-] \033[31mInvalid parameters! Enter "-h" or "--help" to view valid parameters.\033[m')
        else:
            try:
                if len(argv) >= 3:
                    if arg1 == '-l' or arg1 == '--link':
                        url = arg2
                        response = get(url)

                        if len(argv) >= 4:
                            if arg3 == '-hd':
                                try:
                                    link = search ('hd_src:"(.+?)"', response.text)[1]
                                except:
                                    print("\n\033[31m[-] This video doesn't have this quality, downloading the best quality.\033[m")
                                    link = search ('sd_src:"(.+?)"', response.text)[1]
                            elif arg3 == '-sd':
                                try:
                                    link = search ('sd_src:"(.+?)"', response.text)[1]
                                except:
                                    print("\n\033[31m[-] This video doesn't have this quality.\033[m")
                                    link = search ('hd_src:"(.+?)"', response.text)[1]
                            else:
                                print('\n\033[31m[-] Invalid argument, downloading best quality (File name argument before Quality argument).\033[m')
                                
                                try:
                                    link = search ('hd_src:"(.+?)"', response.text)[1]
                                except:
                                    link = search ('sd_src:"(.+?)"', response.text)[1]
                            if len(argv) >= 6:   
                                if arg4 == '-n' or arg4 == '--name':
                                    print('\n\033[32m[+] Downloading video...\033[m\n')
                                    urlretrieve(link, f"{arg5}.mp4")
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
                            except:
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
    class main:
        try:
            fbdownloader(argv[1], argv[2], argv[3], argv[4], argv[5])
        except IndexError:
            print('\n\033[31m[-] One or more arguments are missing. Enter "-h" or "--help" to view valid parameters.\033[m')