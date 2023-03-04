import sys
import subprocess
import os


clearoutput = lambda: os.system('cls')


def install_package(package: str):
    subprocess.check_call([sys.executable, '-m', '-pip', 'install', package])


def is_installed(package: str):
    try:
        __import__(package)
        return True

    except ImportError:
        return False

    except Exception as ex:
        print(f'[!] Error: {ex}. Package: {package}')


def get_packages_list():
    packageslist = []
    with open('Packages.txt', 'rt') as file:
        packages = file.read().splitlines()
        for package in packages:
            if package and not is_installed(package):
                packageslist.append(package)
    return packageslist


def run():
    packageslist = get_packages_list()

    if not packageslist:
        return print('[!] All packages are already installed!')

    print(f'[!] {len(packageslist)} packages are missing! Without those, you cannot run the scripts from this project. \n')
    print('Would you like to install it? Y/N')

    if input().lower() == 'y':
        for package in packageslist:
            print(f'[+] Installing {package}...')
            install_package(package)
        print(f'[!] {len(packageslist)} has been installed!')


try:
    clearoutput()
    run()

except KeyboardInterrupt:
    print('[!] The operation was cancelled by the user!')

