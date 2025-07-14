from crewai import Agent

def get_feature_extractor_agent():
    return Agent(
        role="Feature Extractor",
        goal="Find major features and functionalities implemented in the code",
        backstory="You extract important features of the project",
        allow_delegation=False,
        verbose=True
    )