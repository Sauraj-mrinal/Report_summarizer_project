def write_markdown(content, output_path="output/summary.md"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Markdown written to {output_path}")