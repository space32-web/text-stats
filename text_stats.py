"""Статистика по тексту: количество строк, слов и символов."""
import sys


def text_stats(text):
    """Возвращает словарь со статистикой текста."""
    return {
        "строк": len(text.splitlines()),
        "слов": len(text.split()),
        "символов": len(text),
    }


def main(path):
    """Читает файл и выводит статистику."""
    try:
        with open(path, encoding="utf-8") as file:
            stats = text_stats(file.read())
    except FileNotFoundError:
        print(f"Файл {path} не найден")
        return
    for name, value in stats.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
