"""Статистика по тексту: строки, слова, символы и частые слова."""
import re
import sys
from collections import Counter


def text_stats(text):
    """Возвращает словарь со статистикой текста."""
    return {
        "строк": len(text.splitlines()),
        "слов": len(text.split()),
        "символов": len(text),
    }


def top_words(text, count=5):
    """Возвращает самые частые слова (без учёта регистра и знаков)."""
    words = re.findall(r"[а-яёa-z]+", text.lower())
    return Counter(words).most_common(count)


def main(path):
    """Читает файл и выводит статистику и частые слова."""
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return
    for name, value in text_stats(text).items():
        print(f"{name}: {value}")
    print("Частые слова:")
    for word, number in top_words(text):
        print(f"  {word} — {number}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
