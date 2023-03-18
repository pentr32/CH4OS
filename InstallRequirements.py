import subprocess
import os


def install_package(package: str):
    subprocess.check_call(['pip', 'install', package])


def is_installed(package: str):
    try:
        __import__(package)
        return True

    except ImportError:
        return False

    except Exception as ex:
        print(f'\n[!] Error: {ex}. Package: {package}')


def get_packages_list():
    packages_list = []
    with open('requirements.txt', 'rt') as file:
        packages = file.read().splitlines()
        for package in packages:
            if package and not is_installed(package):
                packages_list.append(package)
    return packages_list


def run():
    packages_list = get_packages_list()

    if not packages_list:
        return print('\n[!] All packages are already installed!')

    print(f'\n[!] {len(packages_list)} packages are missing! Without those, you cannot run the scripts from this project. \n')
    test = [p for p in packages_list]
    print(test)
    print('Would you like to install it? Y/N')

    if input().lower() == 'y':
        for package in packages_list:
            print(f'\n[+] Installing {package}...')
            install_package(package)
        print(f'\n[!] {len(packages_list)} has been installed!')


try:
    os.system('cls')
    run()

except KeyboardInterrupt:
    print('\n[!] The operation was cancelled by the user!')

