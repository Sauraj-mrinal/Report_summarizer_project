from crewai import Agent

def get_architecture_agent():
    return Agent(
        role="Architecture Analyst",
        goal="Analyze the project architecture like MVC, Monolith, Microservices, etc.",
        backstory="You are an expert in software architectures and design patterns.",
        allow_delegation=False,
        verbose=True
    )