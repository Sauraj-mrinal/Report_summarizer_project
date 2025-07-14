# GitHub Repository Summarizer

The **GitHub Repository Summarizer** is a Python-based tool that analyzes a GitHub repository and generates a detailed summary of its structure, features, and architecture. The output includes a Markdown file and a PDF summarizing the repository.

---

## Features

- **Clone GitHub Repositories**: Automatically clones a GitHub repository to a local directory.
- **Analyze Repository Structure**: Identifies the folder and file structure of the repository.
- **Extract Features**: Extracts key features and functionalities implemented in the code.
- **Analyze Architecture**: Provides insights into the software architecture (e.g., MVC, Monolith, Microservices).
- **Generate Summaries**: Combines all analyses into a Markdown file and a PDF.

---

## Folder Structure

```plaintext
github_repo_summarizer_project/
├── agents/
│   ├── repo_structure_agent.py       # Analyzes folder structure
│   ├── feature_extractor_agent.py    # Extracts features and functionalities
│   ├── architecture_agent.py         # Analyzes software architecture
│   └── summarizer_agent.py           # Combines all insights into a summary
│
├── utils/
│   ├── github_clone.py               # Clones GitHub repositories
│   ├── markdown_writer.py            # Writes Markdown files
│   └── pdf_generator.py              # Generates PDFs from Markdown
│
├── output/
│   ├── summary.md                    # Generated Markdown summary
│   └── summary.pdf                   # Generated PDF summary
│
├── main.py                           # Main script to run the summarizer
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## Requirements

1. Python 3.8 or higher
2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` File
   - Create a `.env` file in the root directory of the project.
   - Add the following fields to the `.env` file:
     ```properties
     model=""
     AZURE_API_KEY=""
     AZURE_API_BASE=""
     AZURE_API_VERSION=""
     ```
   - Replace the placeholders with your actual values:
     - `model`: Specify the model name (e.g., `azure/gpt-4o-mini`).
     - `AZURE_API_KEY`: Add your Azure OpenAI API key.
     - `AZURE_API_BASE`: Add your Azure OpenAI API base URL.
     - `AZURE_API_VERSION`: Add the API version (e.g., `2025-04-27`).

---

## Usage

1. Run the `main.py` script:

```bash
python main.py
```

2. Enter the GitHub repository URL when prompted:
```plaintext
Enter GitHub Repo URL: https://github.com/example/repo
```

3. The script will:
   - Clone the repository.
   - Analyze its structure, features, and architecture.
   - Generate a Markdown summary (`output/summary.md`).
   - Generate a PDF summary (`output/summary.pdf`).

4. Check the `output/` folder for the generated files.

---

### Example Output

#### Markdown Summary (`output/summary.md`)
```markdown
# Repository Summary

## Folder Structure
- agents/
  - repo_structure_agent.py
  - feature_extractor_agent.py
  - architecture_agent.py
  - summarizer_agent.py
- utils/
  - github_clone.py
  - markdown_writer.py
  - pdf_generator.py

## Features
- Clones GitHub repositories.
- Analyzes folder and file structure.
- Extracts key features and functionalities.

## Architecture
- Software architecture: MVC
- Design patterns: Singleton, Factory
```

#### PDF Summary (`output/summary.pdf`)
The PDF contains the same content as the Markdown file but in a printable format.

---

## Troubleshooting

### Common Issues

1. **`wkhtmltopdf` Not Found**:
   - Ensure `wkhtmltopdf` is installed and added to your system's PATH.
   - Alternatively, specify the path manually in `utils/pdf_generator.py`:
     ```python
     config = pdfkit.configuration(wkhtmltopdf=r"C:\path\to\wkhtmltopdf.exe")
     ```

2. **Permission Errors**:
   - Ensure you have write permissions for the `output/` directory.

3. **Python Version**:
   - Ensure you are using Python 3.8 or higher.

---

## Contact

For any questions or issues, please contact [Suraj Kumar] at [1507surajkumar@gmail.com].