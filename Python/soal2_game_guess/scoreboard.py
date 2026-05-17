import json
import os

FILE_NAME = "scores.json"

def load_scores():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_score(nama, score):
    data = load_scores()
    # Update skor jika user sudah ada, atau tambah baru
    user_found = False
    for player in data:
        if player['nama'] == nama:
            player['score'] += score
            user_found = True
            break
    
    if not user_found:
        data.append({"nama": nama, "score": score})
    
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def show_top_5():
    data = load_scores()
    # Urutkan berdasarkan score tertinggi
    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
    
    print("\n" + "="*20)
    print("  === TOP 5 SCORE ===")
    for i, p in enumerate(sorted_data[:5], 1):
        print(f"{i}. {p['nama']} – {p['score']} pts")
    print("="*20 + "\n")