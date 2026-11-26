"""Entry for make.fun "Never Say It Out Loud" (u-pucuys-never-say-it-out-loud-8198c3cd).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = "I don't actually understand your question. I just rearranged words until you nodded."

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
