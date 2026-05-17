from game import play_level
from scoreboard import save_score, show_top_5
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.GREEN + "=== WELCOME TO GUESS BATTLE ===")
    nama = input("Masukkan nama login: ").strip()
    if not nama: nama = "Anonymous"

    total_score = 0
    
    # Level Configuration: (Nama, Range, Max Percobaan)
    levels = [
        ("Level 1", 10, 3),
        ("Level 2", 50, 5),
        ("Level 3", 100, 7)
    ]

    for lvl_name, r_max, attempts in levels:
        score_earned = play_level(lvl_name, r_max, attempts)
        total_score += score_earned
        
        if score_earned == 0:
            print(Fore.RED + "Game Over! Skor Anda terhenti di sini.")
            break
        else:
            print(Fore.BLUE + f"Skor sementara: {total_score}")

    # Simpan dan tampilkan hasil
    save_score(nama, total_score)
    show_top_5()

if __name__ == "__main__":
    main()