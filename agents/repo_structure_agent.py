from crewai import Agent

def get_repo_structure_agent():
    return Agent(
        role="Repo Structure Analyst",
        goal="Analyze folder structure of the project",
        backstory="You are a GitHub repo structure expert. Find main folders and files.",
        allow_delegation=False,
        verbose=True
    )