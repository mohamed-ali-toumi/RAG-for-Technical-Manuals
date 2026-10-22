from pathlib import Path

from docling.document_converter import DocumentConverter


def parse_pdf(pdf_path: str | Path) -> str:
    pdf_file = Path(pdf_path)
    if not pdf_file.is_file():
        raise FileNotFoundError(f"PDF-Datei nicht gefunden: {pdf_file}")

    # Docling liest die PDF-Datei ein und wandelt sie in ein Dokument um.
    converter = DocumentConverter()
    result = converter.convert(pdf_file)
    markdown = result.document.export_to_markdown()

    # Die Vorschau erleichtert die Kontrolle des extrahierten Inhalts.
    print(markdown[:1500])
    return markdown
