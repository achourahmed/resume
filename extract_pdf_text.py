import sys
from pathlib import Path

from pdfminer.high_level import extract_text


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <input.pdf> [output.txt]")
        sys.exit(1)

    input_pdf = Path(sys.argv[1]).expanduser().resolve()
    if not input_pdf.exists():
        print(f"Input PDF not found: {input_pdf}")
        sys.exit(1)

    output_txt = (
        Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) > 2 else input_pdf.with_suffix("")
    )
    # Default output name is <input>_extracted.txt if not provided
    if output_txt.suffix:
        # If a suffix exists, assume it's a file path as provided
        out_path = output_txt
    else:
        out_path = Path(str(output_txt) + "_extracted.txt")

    text = extract_text(str(input_pdf))
    out_path.write_text(text, encoding="utf-8")
    print(f"Wrote extracted text to: {out_path}")


if __name__ == "__main__":
    main()


