from pypdf import PdfReader


def load_pdf():
    pdf_name = input("Enter the PDF filename: ")
    try:
        reader = PdfReader(pdf_name)
        if reader.is_encrypted:
            print("This PDF is password-protected.")
            return []

    except FileNotFoundError:
        print("PDF file not found. Please check the filename.")
        return []
    except Exception as error:
        print(f"Could not read this PDF: {error}")
        return []

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    if not full_text.strip():
        print("No readable text found in this PDF.")
        return []

    # Split text into smaller chunks
    chunk_size = 1000

    chunks = [
        full_text[i : i + chunk_size] for i in range(0, len(full_text), chunk_size)
    ]

    return chunks


if __name__ == "__main__":
    chunks = load_pdf()

    if chunks:
        print("PDF loaded successfully!")
        print(f"Total chunks: {len(chunks)}")
