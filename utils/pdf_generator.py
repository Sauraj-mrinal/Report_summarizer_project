import pdfkit

def generate_pdf_from_markdown(md_path="output/summary.md", pdf_path="output/summary.pdf"):
    with open(md_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    html_content = f"<html><body>{markdown_content.replace('\n', '<br>')}</body></html>"
    pdfkit.from_string(html_content, pdf_path)
    print(f"PDF written to {pdf_path}")