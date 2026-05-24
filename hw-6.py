from colorama import init, Fore, Back, Style

init()

print(Fore.RED + "Red text")
print(Fore.GREEN + "Green text")

print(Back.YELLOW + "Yellow background")

print(Style.BRIGHT + "Bright text")
print(Style.DIM + "Dim text")

print(Style.RESET_ALL + "Normal text")