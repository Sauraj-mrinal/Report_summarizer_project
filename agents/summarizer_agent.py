from crewai import Agent

def get_summarizer_agent():
    return Agent(
        role="Project Summarizer",
        goal="Create a final project summary combining all insights",
        backstory="You are a professional technical writer.",
        allow_delegation=False,
        verbose=True
    )