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
