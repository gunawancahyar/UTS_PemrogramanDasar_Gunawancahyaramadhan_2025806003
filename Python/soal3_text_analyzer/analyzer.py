from collections import Counter

def get_statistics(lines):
    full_text = " ".join(lines)
    words = full_text.split()
    
    # Menghitung frekuensi kata (case-insensitive)
    word_list = [w.lower().strip(".,!?:;\"") for w in words]
    word_counts = Counter(word_list)
    
    return {
        "total_lines": len(lines),
        "total_words": len(words),
        "top_5": word_counts.most_common(5)
    }

def generate_ascii_bar(word, count):
    # Membuat bar grafik sederhana
    bar = "#" * count
    return f"{word:<15} {bar} ({count})"