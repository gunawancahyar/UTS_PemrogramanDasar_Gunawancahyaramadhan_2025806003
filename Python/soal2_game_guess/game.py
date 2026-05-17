import random
from colorama import Fore, Style, init

init(autoreset=True)

def play_level(level_name, range_max, max_attempts):
    print(f"\n--- {Fore.CYAN}{level_name} (1-{range_max}){Style.RESET_ALL} ---")
    print(f"Percobaan: {max_attempts}")
    
    target = random.randint(1, range_max)
    
    for i in range(1, max_attempts + 1):
        try:
            tebakan = int(input(f"Percobaan {i}: Tebak angka: "))
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid!")
            continue
            
        if tebakan == target:
            points = (max_attempts - i + 1) * 10
            print(f"{Fore.GREEN}TEPAT! Anda mendapatkan {points} pts.")
            return points
        elif tebakan < target:
            print(Fore.YELLOW + "Terlalu kecil!")
        else:
            print(Fore.YELLOW + "Terlalu besar!")
            
    print(f"{Fore.RED}Gagal! Angka yang benar adalah {target}.")
    return 0
    