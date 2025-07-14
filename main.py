import os
from crewai import Crew, Task
from utils.github_clone import clone_repo
from utils.markdown_writer import write_markdown
from utils.pdf_generator import generate_pdf_from_markdown
from agents.repo_structure_agent import get_repo_structure_agent
from agents.feature_extractor_agent import get_feature_extractor_agent
from agents.architecture_agent import get_architecture_agent
from agents.summarizer_agent import get_summarizer_agent

def read_repo_files(base_path="repo_clone"):
    content = ""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content += f"\n\n### File: " + file_path.replace("\\", "/") + "\n\n" + f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    return content

def main():
    git_url = input("Enter GitHub Repo URL: ")
    clone_path = clone_repo(git_url)

    # Read entire repo content
    repo_content = read_repo_files(clone_path)

    # Agents
    structure_agent = get_repo_structure_agent()
    feature_agent = get_feature_extractor_agent()
    architecture_agent = get_architecture_agent()
    summarizer_agent = get_summarizer_agent()

    # Create tasks for each agent
    structure_task = Task(
        description="Analyze the folder and file structure of the repo.",
        expected_output="Detailed folder/file structure list.",
        agent=structure_agent,
        inputs={"repo_content": repo_content}
    )

    feature_task = Task(
        description="Identify and extract major features and functionalities in the repo.",
        expected_output="List of major features in the repo.",
        agent=feature_agent,
        inputs={"repo_content": repo_content}
    )

    architecture_task = Task(
        description="Analyze and explain the architecture of the project.",
        expected_output="Explanation of the project architecture.",
        agent=architecture_agent,
        inputs={"repo_content": repo_content}
    )

    summarizer_task = Task(
        description="Combine all analyses and create a final summary in markdown format.",
        expected_output="Final project summary in markdown format.",
        agent=summarizer_agent,
        inputs={"repo_content": repo_content}
    )

    # Crew Setup
    crew = Crew(
        agents=[structure_agent, feature_agent, architecture_agent, summarizer_agent],
        tasks=[structure_task, feature_task, architecture_task, summarizer_task],
        verbose=True
    )

    # Execute the Crew AI process
    result = crew.kickoff(inputs={"repo_content": repo_content})
    result_content = str(result)  # Convert CrewOutput to string

    # Write result to markdown and generate PDF
    os.makedirs("output", exist_ok=True)
    write_markdown(result_content, "output/summary.md")

if __name__ == "__main__":
    main()