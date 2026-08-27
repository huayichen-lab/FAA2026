from pathlib import Path


SOURCE = Path("FAAI_2026_EN.tex")
TARGET = Path("FAAI_2026_en.tex")


def main() -> None:
    """Normalize the existing complete English draft into the deliverable file."""
    text = SOURCE.read_text(encoding="utf-8")

    # Repair a few braces that the translation service detached from the
    # original colour-emphasis groups.
    text = text.replace("called an axiom (axiom)} of this system", "called an axiom of this system")
    text = text.replace(r"{\color\color{blue}", r"{\color{blue}")
    text = text.replace(r"f:\1\\to\1", r"f:\{1,2\}\to\{1,2\}")

    # Machine translation occasionally wrapped whole prose paragraphs in braces.
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("{{") and stripped.endswith("}}"):
            indent = line[: len(line) - len(line.lstrip())]
            stripped = stripped[1:-1]
            while stripped.startswith("{") and stripped.endswith("}"):
                stripped = stripped[1:-1]
            line = indent + stripped
        lines.append(line)

    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
