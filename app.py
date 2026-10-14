import re
from pathlib import Path


def extract_invoice(path: str) -> dict:
    text = Path(path).read_text(encoding="utf-8")

    fields = {
        "invoice_number": r"Invoice Number:\s*(.+)",
        "date": r"Date:\s*(\d{4}-\d{2}-\d{2})",
        "total": r"Total:\s*((?:\d+|\d{1,3}(?:,\d{3})+)\.\d{2})",   
 }

    result = {}

    for field, pattern in fields.items():
        match = re.search(pattern, text)
        if not match:
            raise ValueError(f"Missing invoice field: {field}")
        result[field] = match.group(1)

    result["total"] = float(result["total"].replace(",", ""))
    return result


if __name__ == "__main__":
    print(extract_invoice("sample_invoice.txt"))

# Demo: GitHub Actions checks this project after each push.
