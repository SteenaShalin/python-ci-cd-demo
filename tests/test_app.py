import pytest

from app import extract_invoice


def test_extracts_invoice_fields():
    result = extract_invoice("sample_invoice.txt")

    assert result["invoice_number"] == "TEST-1001"
    assert result["date"] == "2026-10-01"
    assert result["total"] == 118.00


def test_rejects_missing_invoice_field(tmp_path):
    invoice = tmp_path / "bad_invoice.txt"
    invoice.write_text("This is not a complete invoice.")

    with pytest.raises(ValueError, match="invoice_number"):
        extract_invoice(str(invoice))


def test_extracts_total_with_thousands_separator(tmp_path):
    invoice = tmp_path / "large_invoice.txt"
    invoice.write_text(
        "Invoice Number: TEST-2001\n"
        "Date: 2026-10-10\n"
        "Total: 1,234.56\n"
    )

    result = extract_invoice(str(invoice))

    assert result["total"] == 1234.56


def test_rejects_incorrectly_grouped_total(tmp_path):
    invoice = tmp_path / "invalid_total.txt"
    invoice.write_text(
        "Invoice Number: TEST-3001\n"
        "Date: 2026-10-12\n"
        "Total: 12,34.56\n"
    )

    with pytest.raises(ValueError, match="total"):
        extract_invoice(str(invoice))
