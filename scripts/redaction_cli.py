#!/usr/bin/env python3
"""
Kleine CLI, die den Maskierungs-Teil aus redaction-script-pii-llm.ipynb nachbildet.
Input -> PII-Maskierung -> Ausgabe des maskierten Texts und der Trefferzahlen.
"""
import argparse
import re
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Tuple

# Regex exakt wie im Notebook
EMAIL = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
ID = re.compile(r"(ID[-:]?\s?\d{3,}|TK-\d{3,}|\d{4}-LLM)")
NAME = re.compile(r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b")


@dataclass
class MaskResult:
    masked: str
    counts: Dict[str, int]


def mask_pii(text: str) -> MaskResult:
    """Maskiert E-Mails, IDs und Namen analog zum Notebook."""
    counts = Counter()

    def repl_email(_match):
        counts["email"] += 1
        return "[EMAIL]"

    def repl_id(_match):
        counts["id"] += 1
        return "[ID]"

    def repl_name(_match):
        counts["name"] += 1
        return "[NAME]"

    masked = EMAIL.sub(repl_email, text)
    masked = ID.sub(repl_id, masked)
    masked = NAME.sub(repl_name, masked)
    return MaskResult(masked=masked, counts=dict(counts))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Maskiert PII (E-Mail, ID, Name) wie im Notebook redaction-script-pii-llm.ipynb"
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="Text, der maskiert werden soll. Wenn leer, wird STDIN gelesen oder interaktiv abgefragt.",
    )
    return parser.parse_args()


def read_text(args: argparse.Namespace) -> str:
    if args.text:
        return " ".join(args.text)
    try:
        import sys

        if not sys.stdin.isatty():
            return sys.stdin.read()
    except Exception:
        pass
    return input("Text eingeben: ")


def main():
    args = parse_args()
    text = read_text(args)
    result = mask_pii(text)

    print("=== Maskiertes Ergebnis ===")
    print(result.masked if result.masked.strip() else "Keine Eingabe erkannt.")
    print("\n=== Treffer ===")
    for key in ("email", "id", "name"):
        print(f"{key}: {result.counts.get(key, 0)}")


if __name__ == "__main__":
    main()
